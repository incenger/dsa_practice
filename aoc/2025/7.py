import collections
import functools

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid


def part_1(file):
    grid = read_input(file)
    M, N = len(grid), len(grid[0])
    start = (0, grid[0].index('S'))

    queue = collections.deque()
    queue.append(start)
    split_count = 0
    while queue:
        row, col = queue.popleft()
        if row == M - 1:
            continue
        if grid[row + 1][col] == '.':
            queue.append((row + 1, col))
            grid[row + 1][col] = "|"
        elif grid[row + 1][col] == "^":
            split_count += 1
            if col > 0:
                queue.append((row + 1, col - 1))
                grid[row + 1][col - 1] = "|"
            if col < N - 1:
                queue.append((row + 1, col + 1))
                grid[row + 1][col + 1] = "|"

    print(f"Part 1: {split_count}")


def part_2(file):
    grid = read_input(file)
    M, N = len(grid), len(grid[0])
    start = (0, grid[0].index('S'))

    @functools.cache
    def dfs(row, col):
        if col < 0 or col >= N:
            return 0
        if row == M - 1:
            return 1
        if grid[row + 1][col] == '.':
            return dfs(row + 1, col)
        if grid[row + 1][col] == "^":
            return dfs(row + 1, col - 1) + dfs(row + 1, col + 1)
        return 0

    timelines = dfs(*start)
    print(f"Part 2: {timelines}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
