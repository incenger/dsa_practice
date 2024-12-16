"""
time python3 15.py
python3 15.py  0.03s user 0.02s system 81% cpu 0.061 total
"""
import heapq
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INITIAL_FACING = 1


def read_input(file):
    maze = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            maze.append(list(line))
    return maze


def get_score(facing_dir, moving_dir):
    frow, fcol = DIRS[facing_dir]
    mrow, mcol = DIRS[moving_dir]
    dot_product = frow * mrow + fcol * mcol
    if dot_product == 1:
        return 1
    elif dot_product == -1:
        return 2001
    return 1001


def dijkstra(maze, start_row, start_col):
    M, N = len(maze), len(maze[0])
    path_to = collections.defaultdict(set)
    scores = collections.defaultdict(lambda: float('inf'))
    scores[(start_row, start_col, 1)] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, start_row, start_col, INITIAL_FACING))
    min_score = float('inf')
    ends = set()

    while min_heap:
        score, row, col, facing = heapq.heappop(min_heap)

        if maze[row][col] == 'E':
            min_score = score
            ends.add((row, col, facing))

        if score > min_score:
            continue

        for moving_dir, (drow, dcol) in enumerate(DIRS):
            next_row = row + drow
            next_col = col + dcol
            if maze[next_row][next_col] == '#':
                continue
            score_gained = get_score(facing, moving_dir)
            if score + score_gained < scores[(next_row, next_col, moving_dir)]:
                scores[(next_row, next_col, moving_dir)] = score + score_gained
                heapq.heappush(min_heap,
                               (scores[(next_row, next_col, moving_dir)],
                                next_row, next_col, moving_dir))
                path_to[(next_row, next_col, moving_dir)] = {(row, col, facing)
                                                             }
            elif score + score_gained == scores[(next_row, next_col,
                                                 moving_dir)]:
                path_to[(next_row, next_col, moving_dir)].add(
                    (row, col, facing))
    return min_score, path_to, ends


def part_1(file):
    maze = read_input(file)
    M, N = len(maze), len(maze[0])
    start_row, start_col = -1, -1
    end_row, end_col = -1, -1
    for row in range(M):
        for col in range(N):
            if maze[row][col] == 'S':
                start_row, start_col = row, col
            if maze[row][col] == 'E':
                end_row, end_col = row, col

    min_score, _, _ = dijkstra(maze, start_row, start_col)
    print("ANSWER", min_score)


def part_2(file):
    maze = read_input(file)
    M, N = len(maze), len(maze[0])
    start_row, start_col = -1, -1
    end_row, end_col = -1, -1
    for row in range(M):
        for col in range(N):
            if maze[row][col] == 'S':
                start_row, start_col = row, col
            if maze[row][col] == 'E':
                end_row, end_col = row, col

    min_score, path_to, end_states = dijkstra(maze, start_row, start_col)

    queue = collections.deque(end_states)
    visited_states = set(end_states)
    seats = set()
    while queue:
        row, col, facing_dir = queue.popleft()
        seats.add((row, col))
        for prev_row, prev_col, prev_dir in path_to[(row, col, facing_dir)]:
            if (prev_row, prev_col, prev_dir) not in visited_states:
                queue.append((prev_row, prev_col, prev_dir))
                visited_states.add((prev_row, prev_col, prev_dir))
    print("ANSWER", len(seats))


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
