"""
time python3 10.py
python3 10.py  0.03s user 0.02s system 85% cpu 0.052 total
"""
import collections
import functools

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input(file):
    height_map = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            height_map.append([int(ch) if ch != '.' else -1 for ch in line])
    return height_map


def part_1(file):
    height_map = read_input(file)
    m, n = len(height_map), len(height_map[0])

    @functools.cache
    def dfs(row, col):
        if height_map[row][col] == 9:
            return set([(row, col)])

        trailheads = set()
        for drow, dcol in DIRS:
            next_row = row + drow
            next_col = col + dcol
            if not (0 <= next_row < m and 0 <= next_col < n):
                continue
            if height_map[next_row][next_col] != height_map[row][col] + 1:
                continue

            trailheads |= dfs(next_row, next_col)
        return trailheads

    answer = 0
    for row in range(m):
        for col in range(n):
            if height_map[row][col] == 0:
                answer += len(dfs(row, col))

    print("ANSWER:", answer)


def part_2(file):
    height_map = read_input(file)
    m, n = len(height_map), len(height_map[0])

    @functools.cache
    def dfs(row, col):
        if height_map[row][col] == 9:
            return 1

        score = 0
        for drow, dcol in DIRS:
            next_row = row + drow
            next_col = col + dcol
            if not (0 <= next_row < m and 0 <= next_col < n):
                continue
            if height_map[next_row][next_col] != height_map[row][col] + 1:
                continue
            score += dfs(next_row, next_col)
        return score

    answer = 0
    for row in range(m):
        for col in range(n):
            if height_map[row][col] == 0:
                answer += dfs(row, col)

    print("ANSWER:", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
