import heapq
import math

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


class DSU():

    def __init__(self, n):
        self.n = n
        self.size = [1] * n
        self.root = list(range(n))
        self.root_count = n

    def find_root(self, u):
        if self.root[u] == u:
            return u
        self.root[u] = self.find_root(self.root[u])
        return self.root[u]

    def is_connected(self, u, v):
        return self.find_root(u) == self.find_root(v)

    def connect(self, u, v):
        root_u = self.find_root(u)
        root_v = self.find_root(v)
        if root_u == root_v:
            return False
        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u
        self.root[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        self.root_count -= 1
        return True

    def get_root_sizes(self):
        return [self.size[i] for i in range(self.n) if self.find_root(i) == i]


def read_input(file):
    box_coords = []
    with open(file, "r") as f:
        for line in f.readlines():
            box_coords.append(list(map(int, line.strip().split(","))))
    return box_coords


def l2_sqdist(coord_a, coord_b):
    return sum((a - b)**2 for a, b in zip(coord_a, coord_b))


def part_1(file, conn_pairs):
    box_coords = read_input(file)
    B = len(box_coords)
    N_MAX_CIRCUIT = 3
    min_heap = []
    for i in range(B):
        for j in range(i + 1, B):
            heapq.heappush(min_heap,
                           (l2_sqdist(box_coords[i], box_coords[j]), i, j))

    dsu = DSU(B)
    while conn_pairs > 0:
        _, u, v = heapq.heappop(min_heap)
        dsu.connect(u, v)
        conn_pairs -= 1

    circuit_sizes = dsu.get_root_sizes()
    circuit_sizes.sort()
    answer = math.prod(circuit_sizes[-N_MAX_CIRCUIT:])
    print(f"Answer: {answer}")


def part_2(file):
    box_coords = read_input(file)
    B = len(box_coords)
    min_heap = []
    for i in range(B):
        for j in range(i + 1, B):
            heapq.heappush(min_heap,
                           (l2_sqdist(box_coords[i], box_coords[j]), i, j))

    answer = 0
    dsu = DSU(B)
    while min_heap:
        _, u, v = heapq.heappop(min_heap)
        dsu.connect(u, v)
        if dsu.root_count == 1:
            answer = box_coords[u][0] * box_coords[v][0]
            break

    print(f"Answer: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE, conn_pairs=1000)
    part_2(INPUT_FILE)
