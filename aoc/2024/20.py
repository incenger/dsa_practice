"""
"""
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input(file):
    racetrack = []
    with open(file, "r") as f:
        for line in f.readlines():
            racetrack.append(list(line.strip()))
    return racetrack


def bfs(racetrack, start):
    M, N = len(racetrack), len(racetrack[0])
    start_row, start_col = start
    queue = collections.deque([(start_row, start_col)])
    dist = [[float('inf')] * N for _ in range(M)]
    dist[start_row][start_col] = 0
    while queue:
        row, col = queue.popleft()
        if racetrack[row][col] == '#':
            continue
        for dr, dc in DIRS:
            next_row = row + dr
            next_col = col + dc
            if 0 <= next_row < M and 0 <= next_row < N \
            and dist[next_row][next_col] == float('inf'):
                dist[next_row][next_col] = dist[row][col] + 1
                queue.append((next_row, next_col))
    return dist


def part_1(file):
    """
    Two-second phase corresponds to unblock a single wall
    """
    racetrack = read_input(file)
    M, N = len(racetrack), len(racetrack[0])
    start, end = None, None
    wall_to_try = []
    for row in range(M):
        for col in range(N):
            if racetrack[row][col] == 'S':
                start = (row, col)
            if racetrack[row][col] == 'E':
                end = (row, col)

            if racetrack[row][
                    col] == '#' and 0 < row < M - 1 and 0 < col < N - 1:
                wall_to_try.append((row, col))

    dist_from_start = bfs(racetrack, start)
    dist_from_end = bfs(racetrack, end)
    orig_dist = dist_from_start[end[0]][end[1]]

    save_count = collections.Counter()

    for wall_row, wall_col in wall_to_try:
        new_dist = dist_from_start[wall_row][wall_col] + dist_from_end[
            wall_row][wall_col]
        save_count[orig_dist - new_dist] += 1
    answer = sum(count for save, count in save_count.items() if save >= 100)
    print("ANSWER", answer)


def part_2(file):
    pass


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    # part_2(SAMPLE_FILE)
    # part_2(INPUT_FILE)