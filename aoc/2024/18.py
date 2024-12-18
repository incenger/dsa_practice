"""
linear_brute_force:
    time python3 18.py
    python3 18.py  7.64s user 0.14s system 98% cpu 7.901 total

binary_search:
    time python3 18.py
    python3 18.py  0.04s user 0.02s system 83% cpu 0.067 total

dsu:
    time python3 18.py
    python3 18.py  0.04s user 0.02s system 89% cpu 0.069 total
"""
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRS_8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def read_input(file):
    byte_locations = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            byte_locations.append(tuple(map(int, line.split(","))))
    return byte_locations


def bfs(mem_size, byte_locations, num_bytes):
    memory_space = [['.'] * mem_size for _ in range(mem_size)]
    for row, col in byte_locations[:num_bytes]:
        memory_space[row][col] = '#'

    queue = collections.deque([(0, 0, 0)])
    visited = [[False] * mem_size for _ in range(mem_size)]
    visited[0][0] = True
    answer = None
    while queue and answer is None:
        row, col, step = queue.popleft()
        for drow, dcol in DIRS:
            next_row = row + drow
            next_col = col + dcol

            if next_row == mem_size - 1 and next_col == mem_size - 1:
                answer = step + 1

            if 0 <= next_row < mem_size and 0 <= next_col < mem_size \
            and memory_space[next_row][next_col] == '.' \
            and not visited[next_row][next_col]:
                queue.append((next_row, next_col, step + 1))
                visited[next_row][next_col] = True
    return answer


def part_1(file, mem_size, num_bytes):
    byte_locations = read_input(file)
    answer = bfs(mem_size, byte_locations, num_bytes)
    print("ANSWER", answer)


class DSU():

    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n

    def find_root(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find_root(self.root[x])
        return self.root[x]

    def union(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)

        if self.size[x] > self.size[y]:
            x, y = y, x

        self.root[x] = y
        self.size[y] += self.size[x]

    def is_connected(self, x, y):
        return self.find_root(x) == self.find_root(y)


def part_2(file, mem_size):
    byte_locations = read_input(file)

    def linear_brute_force():
        for num_bytes in range(1, len(byte_locations) + 1):
            if bfs(mem_size, byte_locations, num_bytes) is None:
                answer = num_bytes
                return answer

    def binary_search():
        low, high = 1, len(byte_locations)

        while low < high:
            mid = (low + high) // 2
            if bfs(mem_size, byte_locations, mid):
                low = mid + 1
            else:
                high = mid
        return low

    def dsu():

        top, bottom, left, right = [
            mem_size * mem_size + idx for idx in range(4)
        ]
        blocker_dsu = DSU(mem_size * mem_size + 4)
        blockers = set()
        for idx, (row, col) in enumerate(byte_locations, start=1):
            blockers.add((row, col))
            byte_id = row * mem_size + col
            for drow, dcol in DIRS_8:
                next_row = row + drow
                next_col = col + dcol
                next_byte_id = next_row * mem_size + next_col

                if next_row == -1:
                    blocker_dsu.union(top, byte_id)
                if next_row == mem_size:
                    blocker_dsu.union(bottom, byte_id)
                if next_col == -1:
                    blocker_dsu.union(left, byte_id)
                if next_col == mem_size:
                    blocker_dsu.union(right, byte_id)

                if 0 <= next_row < mem_size and 0 <= next_row < mem_size and (
                        next_row, next_col) in blockers:
                    blocker_dsu.union(next_byte_id, byte_id)


            if blocker_dsu.is_connected(top, bottom) \
                or blocker_dsu.is_connected(left, right) \
                or blocker_dsu.is_connected(bottom, right):
                return idx
        return None

    answer = byte_locations[dsu() - 1]
    print("ANSWER", ",".join(map(str, answer)))


if __name__ == "__main__":
    part_1(SAMPLE_FILE, 7, 12)
    part_1(INPUT_FILE, 71, 1024)
    part_2(SAMPLE_FILE, 7)
    part_2(INPUT_FILE, 71)
