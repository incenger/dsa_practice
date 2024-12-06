import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input(file):
    problem_map = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            problem_map.append(list(line))
    return problem_map


def part_1(file):
    problem_map = read_input(file)
    m, n = len(problem_map), len(problem_map[0])

    start_row, start_col = None, None
    for r in range(m):
        for c in range(n):
            if problem_map[r][c] == '^':
                start_row, start_col = r, c

    cur_row, cur_col = start_row, start_col
    cur_direction_idx = 0
    visited = set()
    while True:
        visited.add((cur_row, cur_col))
        next_row = cur_row + DIRS[cur_direction_idx][0]
        next_col = cur_col + DIRS[cur_direction_idx][1]
        if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
            break
        if problem_map[next_row][next_col] == '#':
            cur_direction_idx = (cur_direction_idx + 1) % len(DIRS)
        else:
            cur_row, cur_col = next_row, next_col

    answer = len(visited)
    print("ANSWER:", answer)


def run_cycle(problem_map, start_row, start_col, start_dir, visited):
    m, n = len(problem_map), len(problem_map[0])
    cur_row, cur_col, cur_dir = start_row, start_col, start_dir
    while True:
        visited.add((cur_row, cur_col, cur_dir))
        next_row = cur_row + DIRS[cur_dir][0]
        next_col = cur_col + DIRS[cur_dir][1]
        if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
            return False
        if problem_map[next_row][next_col] == '#':
            cur_dir = (cur_dir + 1) % len(DIRS)
        else:
            if (next_row, next_col, cur_dir) in visited:
                return True
            cur_row, cur_col = next_row, next_col
    return False


def part_2(file):
    """
    Brute force
    """
    problem_map = read_input(file)
    m, n = len(problem_map), len(problem_map[0])

    start_row, start_col = None, None
    for r in range(m):
        for c in range(n):
            if problem_map[r][c] == '^':
                start_row, start_col = r, c

    cur_row, cur_col = start_row, start_col
    cur_direction_idx = 0
    visited = set()
    answer = 0
    tried_new_obstacle = set()
    while True:
        visited.add((cur_row, cur_col))
        next_row = cur_row + DIRS[cur_direction_idx][0]
        next_col = cur_col + DIRS[cur_direction_idx][1]
        if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
            break
        if problem_map[next_row][next_col] == '#':
            cur_direction_idx = (cur_direction_idx + 1) % len(DIRS)
        else:
            # Place a new obstacle
            if (next_row, next_col) not in tried_new_obstacle:
                tried_new_obstacle.add((next_row, next_col))
                problem_map[next_row][next_col] = '#'
                if run_cycle(problem_map, cur_row,
                             cur_col, (cur_direction_idx + 1) % len(DIRS),
                             set(visited)):
                    answer += 1
                problem_map[next_row][next_col] = '.'
            # Advance
            cur_row, cur_col = next_row, next_col

    print("ANSWER:", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
