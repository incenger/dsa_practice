SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
ROLLS_LIMIT = 4


def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid


def count_rolls(grid, row, col):
    M, N = len(grid), len(grid[0])
    rolls = 0
    for dr, dc in DIRS:
        nrow = row + dr
        ncol = col + dc
        if 0 <= nrow < M and 0 <= ncol < N and grid[nrow][ncol] == '@':
            rolls += 1
    return rolls


def part_1(file):
    grid = read_input(file)
    M, N = len(grid), len(grid[0])
    answer = 0
    for row in range(M):
        for col in range(N):
            if grid[row][col] == '.':
                continue
            rolls = count_rolls(grid, row, col)
            answer += 1 if rolls < ROLLS_LIMIT else 0
    print(f"Part 1: {answer}")


def part_2(file):
    grid = read_input(file)
    M, N = len(grid), len(grid[0])
    answer = 0
    loop_count = 0

    while True:
        remove = 0
        for row in range(M):
            for col in range(N):
                if grid[row][col] == '.':
                    continue
                rolls = count_rolls(grid, row, col)
                if rolls < ROLLS_LIMIT:
                    remove += 1
                    grid[row][col] = '.'
        answer += remove
        loop_count += 1
        if remove == 0:
            break
    print(f"Part 2: Loop Count: {loop_count} | Answer: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
