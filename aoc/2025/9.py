from collections import namedtuple
import heapq

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

Point = namedtuple("Point", ["x", "y"])


def read_input(file):
    tiles = []
    with open(file, "r") as f:
        for line in f.readlines():
            coords = list(map(int, line.strip().split(",")))
            tiles.append(Point(*coords))
    return tiles


def area(a, b):
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def part_1(file):
    tiles = read_input(file)
    N = len(tiles)
    max_area = 0
    for i in range(N):
        for j in range(i + 1, N):
            max_area = max(max_area, area(tiles[i], tiles[j]))
    print(f"Part 1: {max_area}")


def intersect(p_min, p_max, edges):
    """Check if a rectangle intersects with any edges of the polygon

    We can use AABB collision detection algorithm as all the rectangles are axis-aligned.
    """
    for p_0, p_1 in edges:
        if p_min.x < p_1.x and p_max.x > p_0.x and p_min.y < p_1.y and p_max.y > p_0.y:
            return True
    return False


def part_2(file):
    tiles = read_input(file)

    edges = []
    p_0 = tiles[0]
    for i in range(1, len(tiles) + 1):
        p_1 = tiles[i % len(tiles)]
        x_min, x_max = min(p_0.x, p_1.x), max(p_0.x, p_1.x)
        y_min, y_max = min(p_0.y, p_1.y), max(p_0.y, p_1.y)
        edges.append((Point(x_min, y_min), Point(x_max, y_max)))
        p_0 = p_1

    areas = []
    N = len(tiles)
    for i in range(N):
        for j in range(i + 1, N):
            p_min = Point(min(tiles[i].x, tiles[j].x),
                          min(tiles[i].y, tiles[j].y))
            p_max = Point(max(tiles[i].x, tiles[j].x),
                          max(tiles[i].y, tiles[j].y))
            heapq.heappush(areas, (-area(p_min, p_max), p_min, p_max))

    while areas and intersect(areas[0][1], areas[0][2], edges):
        heapq.heappop(areas)

    print(f"Part 2: {-areas[0][0]}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
