"""
"""

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input(file):
    garden = []
    with open(file, "r") as f:
        for line in f.readlines():
            garden.append(list(line.strip()))
    return garden


def part_1(file):
    garden = read_input(file)
    m, n = len(garden), len(garden[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(row, col):
        visited[row][col] = True
        area = 1
        peri = 0

        for dr, dc in DIRS:
            next_row = row + dr
            next_col = col + dc

            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or garden[
                    next_row][next_col] != garden[row][col]:
                peri += 1
            elif not visited[next_row][next_col]:
                next_area, next_peri = dfs(next_row, next_col)
                peri += next_peri
                area += next_area
        return area, peri

    answer = 0
    for row in range(m):
        for col in range(n):
            if not visited[row][col]:
                area, peri = dfs(row, col)
                answer += area * peri
    print("ANSWER", answer)


def part_2(file):
    pass


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    # part_2(SAMPLE_FILE)
    # part_2(INPUT_FILE)
