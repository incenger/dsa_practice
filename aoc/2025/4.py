import collections

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
    if grid[row][col] == '.':
        return M * N + 1
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
    rolls = [[0] * N for _ in range(M)]
    queue = collections.deque()

    for row in range(M):
        for col in range(N):
            rolls[row][col] = count_rolls(grid, row, col)
            if rolls[row][col] < ROLLS_LIMIT:
                queue.append((row, col))

    answer = 0
    while queue:
        answer += 1
        row, col = queue.popleft()
        grid[row][col] = '.'
        for dr, dc in DIRS:
            nrow = row + dr
            ncol = col + dc
            if 0 <= nrow < M and 0 <= ncol < N and grid[nrow][ncol] == '@':
                if rolls[nrow][ncol] == ROLLS_LIMIT:
                    queue.append((nrow, ncol))
                rolls[nrow][ncol] -= 1
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
