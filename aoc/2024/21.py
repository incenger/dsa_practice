"""
time python3 21.py
python3 21.py  0.03s user 0.02s system 88% cpu 0.051 tota
"""
import functools
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = {"^": (-1, 0), "<": (0, -1), "v": (1, 0), ">": (0, 1)}


def read_input(file):
    codes = []
    with open(file, "r") as f:
        for line in f.readlines():
            codes.append(line.strip())
    return codes


def compute_paths(pad):
    # Compute all the valid shortest path between two keys on a pad
    M, N = len(pad), len(pad[0])

    pad_key_to_location = {
        pad[row][col]: (row, col)
        for row in range(len(pad))
        for col in range(len(pad[0]))
    }

    def bfs(start_key):
        start_row, start_col = pad_key_to_location[start_key]
        dist = [[float('inf')] * N for _ in range(M)]
        dist[start_row][start_col] = 0
        queue = collections.deque([(start_row, start_col, "")])
        paths_to = collections.defaultdict(list)
        paths_to[start_key] = "A"
        while queue:
            row, col, path = queue.popleft()
            for dir_code, (drow, dcol) in DIRS.items():
                n_row = row + drow
                n_col = col + dcol
                if n_row < 0 or n_row >= M or n_col < 0 or n_col >= N:
                    continue
                if pad[n_row][n_col] == 'X':
                    continue
                if dist[row][col] + 1 <= dist[n_row][n_col]:
                    queue.append((n_row, n_col, path + dir_code))
                    dist[n_row][n_col] = dist[row][col] + 1
                    paths_to[pad[n_row][n_col]].append(path + dir_code + 'A')

        return paths_to

    paths = {}
    for row in range(M):
        for col in range(N):
            if pad[row][col] != 'X':
                paths[pad[row][col]] = bfs(pad[row][col])
    return paths


NUMPAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["X", "0", "A"]]
DIRPAD = [["X", "^", "A"], ["<", "v", ">"]]
NUMPAD_PATHS = compute_paths(NUMPAD)
DIRPAD_PATHS = compute_paths(DIRPAD)


def get_all_numpad_paths(code):
    prev = "A"
    queue = [""]
    for key in code:
        paths = NUMPAD_PATHS[prev][key]
        next_queue = []
        for cur_path in queue:
            for next_path in paths:
                next_queue.append(cur_path + next_path)
        queue = next_queue
        prev = key
    return queue


@functools.cache
def compute_num_dir_presses(dir_path, depth):
    prev = 'A'
    num_presses = 0
    if depth == 1:
        for key in dir_path:
            # At one recursion level, all paths considered equally
            num_presses += len(DIRPAD_PATHS[prev][key][0])
            prev = key
    else:
        for key in dir_path:
            num_presses += min(
                compute_num_dir_presses(path, depth - 1)
                for path in DIRPAD_PATHS[prev][key])
            prev = key
    return num_presses


def part_1(file):
    codes = read_input(file)
    answer = 0
    NUM_ROBOTS = 3

    for code in codes:
        all_numpad_paths = get_all_numpad_paths(code)
        optimal_key_presses = min(
            compute_num_dir_presses(numpad_path, depth=NUM_ROBOTS - 1)
            for numpad_path in all_numpad_paths)
        digits = int("".join(ch for ch in code if ch.isdigit()))
        answer += digits * optimal_key_presses
    print("ANSWER", answer)


def part_2(file):
    codes = read_input(file)
    answer = 0
    NUM_ROBOTS = 26

    for code in codes:
        all_numpad_paths = get_all_numpad_paths(code)
        optimal_key_presses = min(
            compute_num_dir_presses(numpad_path, depth=NUM_ROBOTS - 1)
            for numpad_path in all_numpad_paths)
        digits = int("".join(ch for ch in code if ch.isdigit()))
        answer += digits * optimal_key_presses
    print("ANSWER", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
