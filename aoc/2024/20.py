"""
time python3 20.py
python3 20.py  1.42s user 0.03s system 98% cpu 1.473 total
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

    save_count = collections.defaultdict(int)

    for wall_row, wall_col in wall_to_try:
        new_dist = dist_from_start[wall_row][wall_col] + dist_from_end[
            wall_row][wall_col]
        save_count[orig_dist - new_dist] += 1
    answer = sum(count for save, count in save_count.items() if save >= 100)
    print("ANSWER", answer)


def part_2(file):
    racetrack = read_input(file)
    M, N = len(racetrack), len(racetrack[0])
    start, end = None, None
    wall_to_try = []
    spaces = []
    for row in range(M):
        for col in range(N):
            if racetrack[row][col] == 'S':
                start = (row, col)
            if racetrack[row][col] == 'E':
                end = (row, col)
            if racetrack[row][col] != '#':
                spaces.append((row, col))

    dist = bfs(racetrack, start)

    PHASE_LIMIT = 20

    def get_phase_end(start_row, start_col):
        for drow in range(-PHASE_LIMIT, PHASE_LIMIT + 1):
            max_dcol = PHASE_LIMIT - abs(drow)
            end_row = start_row + drow
            if end_row < 0 or end_row >= M:
                continue
            for dcol in range(-max_dcol, max_dcol + 1):
                end_col = start_col + dcol
                if end_col < 0 or end_col >= N:
                    continue
                if racetrack[end_row][end_col] != '#' \
                    and dist[end_row][end_col] >= dist[start_row][start_col]:
                    yield (end_row, end_col)

    # Brute force for all possible starting and ending position of the cheat
    save_count = collections.defaultdict(int)
    for phase_start_row, phase_start_col in spaces:
        for phase_end_row, phase_end_col in get_phase_end(
                phase_start_row, phase_start_col):
            orig_dist = dist[phase_end_row][phase_end_col] - dist[
                phase_start_row][phase_start_col]
            if orig_dist <= 0:
                continue
            direct_dist = abs(phase_end_row -
                              phase_start_row) + abs(phase_start_col -
                                                     phase_end_col)
            if direct_dist <= PHASE_LIMIT:
                save = (orig_dist - direct_dist)
                save_count[save] += 1

    for threshold in [50, 100]:
        answer = sum(count for save, count in save_count.items()
                     if save >= threshold)
        print(f"ANSWER({threshold})", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
