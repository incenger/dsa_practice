"""
time python3 14.py
python3 14.py  0.03s user 0.02s system 88% cpu 0.054 total
"""
import re
import math
import itertools

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    robots = []
    robot_info_regex = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            robot_info = robot_info_regex.findall(line)[0]
            robots.append(list(map(int, robot_info)))
    return robots


def part_1(file, N_ROWS, N_COLS):
    QUADRANT_ROWS = N_ROWS // 2
    QUADRANT_COLS = N_COLS // 2
    robots = read_input(file)
    STEPS = 100
    quadrant = [[0, 0], [0, 0]]

    for col, row, v_col, v_row in robots:
        row_dest = (row + STEPS * v_row) % N_ROWS
        col_dest = (col + STEPS * v_col) % N_COLS

        if row_dest == QUADRANT_ROWS or col_dest == QUADRANT_COLS:
            continue
        quadrant[row_dest // (QUADRANT_ROWS + 1)][col_dest //
                                                  (QUADRANT_COLS + 1)] += 1

    answer = math.prod(itertools.chain.from_iterable(quadrant))
    print("ANSWER", answer)


def part_2(file, N_ROWS, N_COLS, print_trace=False):
    QUADRANT_ROWS = N_ROWS // 2
    QUADRANT_COLS = N_COLS // 2
    robots = read_input(file)
    MAX_STEPS = 50000
    quadrant = [[0, 0], [0, 0]]

    if print_trace:
        for step in range(1, MAX_STEPS + 1):
            print("STEP", step)
            grid = [['.'] * N_COLS for _ in range(N_ROWS)]
            for col, row, v_col, v_row in robots:
                row_dest = (row + step * v_row) % N_ROWS
                col_dest = (col + step * v_col) % N_COLS

                grid[row_dest][col_dest] = 'O'
            for grid_row in grid:
                print("".join(grid_row))
    print("ASNWER", 6644)


if __name__ == "__main__":
    part_1(SAMPLE_FILE, 7, 11)
    part_1(INPUT_FILE, 103, 101)
    part_2(INPUT_FILE, 103, 101)
