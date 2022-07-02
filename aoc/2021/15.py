from collections import defaultdict
import heapq

"""
N^2 vertices
N^2 * 4 edges
Find the shortest path from 0 to N^2 - 1

We don't need to build the graph, right?
"""


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()

    grid = [list(map(int, l.strip())) for l in lines]

    return grid


DIRR = [-1, 0, 0, 1]
DIRC = [0, -1, 1, 0]


def part_1(grid):
    m = len(grid)
    n = len(grid[0])

    # Dikstra
    dist = defaultdict(lambda: float("inf"))
    dist[(0, 0)] = 0

    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, (0, 0)))

    while len(pq):
        d, (r, c) = heapq.heappop(pq)
        if (r, c) == (m - 1, n - 1):
            break

        if d != dist[(r, c)]:
            # Ignore handled vertex
            # Helps avoid the complexity goes up to O(nm)
            continue

        for dr, dc in zip(DIRR, DIRC):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < m and 0 <= nc < n:
                d_to = grid[nr][nc]

                if dist[(r, c)] + d_to < dist[(nr, nc)]:
                    dist[(nr, nc)] = dist[(r, c)] + d_to
                    heapq.heappush(pq, (dist[(nr, nc)], (nr, nc)))

    return dist[(m - 1, n - 1)]


def part_2(grid):
    m = len(grid)
    n = len(grid[0])

    large_grid = [[0] * (5 * n) for _ in range(5 * m)]

    for i in range(5 * m):
        for j in range(5 * n):
            correspond_i = i % m
            correspond_j = j % n
            repeat_i = i // m
            repeat_j = j // n

            large_grid[i][j] = grid[correspond_i][correspond_j] + repeat_i + repeat_j
            if large_grid[i][j] > 9:
                large_grid[i][j] = large_grid[i][j] % 10 + 1
    return part_1(large_grid)


if __name__ == "__main__":
    grid = read_input("input.txt")
    import time
    tick = time.perf_counter()
    print(part_2(grid))
    tock = time.perf_counter()
    print(tock-tick)
