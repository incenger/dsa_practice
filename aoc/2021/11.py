def read_input(file):
    with open(file, "r") as f:
        grid = [list(map(int, [int(c) for c in l.strip()])) for l in f.readlines()]
    return grid


DIRR = [-1, -1, -1, 0, 0, 1, 1, 1]
DIRC = [-1, 0, 1, -1, 1, -1, 0, 1]


def part_1(grid):

    # State: 0, 1  - Flash and not flash
    m = len(grid)
    n = len(grid[0])
    count = 0

    def dfs(r, c):
        nonlocal count
        if grid[r][c] < 9:
            grid[r][c] += 1
        else:
            # Flash
            grid[r][c] = 0
            state[r][c] = 1

            count += 1

            for dr, dc in zip(DIRR, DIRC):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and state[nr][nc] == 0:
                    # print("Flash", r, c, "DFS", nr, nc)
                    dfs(nr, nc)

    for step in range(1, 1001):
        state = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if state[r][c] == 0:
                    dfs(r, c)

        all_flash = all([all([grid[r][c] == 0 for c in range(n)]) for r in range(m)])

        if all_flash:
            return step

    return count


if __name__ == "__main__":
    grid = read_input("input.txt")
    print(part_1(grid))
