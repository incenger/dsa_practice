from collections import defaultdict
from bisect import bisect_left


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()

    commands = []
    for line in lines:
        on_off, cubes = line.split()
        xyz = []
        for coord in cubes.split(","):
            low, high = list(map(int, coord[2:].split("..")))
            xyz.append((low, high))
        commands.append((on_off, xyz))

    return commands


def read_input_part_2(file):
    with open(file, "r") as f:
        lines = f.readlines()

    commands = []
    for line in lines:
        on_off, cubes = line.split()
        xyz = []
        for coord in cubes.split(","):
            low, high = list(map(int, coord[2:].split("..")))
            # We increase high by 1 to include all segments from low to high
            xyz.append((low, high + 1))
        commands.append((on_off, xyz))

    return commands


def part_1(commands):
    on_cube = set()

    for on_off, xyz in commands:
        x0, x1 = xyz[0]
        y0, y1 = xyz[1]
        z0, z1 = xyz[2]
        if on_off == "on":
            for i in range(max(-50, x0), min(x1, 50) + 1):
                for j in range(max(-50, y0), min(y1, 50) + 1):
                    for k in range(max(-50, z0), min(z1, 50) + 1):
                        on_cube.add((i, j, k))
        else:
            for i in range(max(-50, x0), min(x1, 50) + 1):
                for j in range(max(-50, y0), min(y1, 50) + 1):
                    for k in range(max(-50, z0), min(z1, 50) + 1):
                        if (i, j, k) in on_cube:
                            on_cube.remove((i, j, k))

    return len(on_cube)


"""
How about one dimension?
Given a list of segments, each turn on or off numbers within that segment, how many points are on after the process finished?
We don't need to care about all the points, we only need to care about end points of each segment since each segment is either on or off. Given a segment, we need to find its two endpoints and mark all end points between them

Generalization for 2 dimension. Iterate over all pairs of end points and count
"""


def part_2(commands):

    endpoints = defaultdict(list)

    for _, xyz in commands:
        (x0, x1), (y0, y1), (z0, z1) = xyz
        endpoints["x"].extend([x0, x1])
        endpoints["y"].extend([y0, y1])
        endpoints["z"].extend([z0, z1])

    for coord in endpoints.values():
        coord.sort()

    n = len(endpoints["x"])
    # We have n-1 segment
    segment = [[[False] * (n - 1) for _ in range(n - 1)] for __ in range(n - 1)]

    for on_off, xyz in commands:
        (x0, x1), (y0, y1), (z0, z1) = xyz
        x0 = bisect_left(endpoints["x"], x0)
        x1 = bisect_left(endpoints["x"], x1)
        y0 = bisect_left(endpoints["y"], y0)
        y1 = bisect_left(endpoints["y"], y1)
        z0 = bisect_left(endpoints["z"], z0)
        z1 = bisect_left(endpoints["z"], z1)

        # We change value of segment from x0 -> x1 - 1 (until the segment ends at x1)
        for x in range(x0, x1):
            for y in range(y0, y1):
                for z in range(z0, z1):
                    segment[x][y][z] = True if on_off == "on" else False

    count = 0

    for x in range(len(segment)):
        for y in range(len(segment)):
            for z in range(len(segment)):
                if segment[x][y][z]:
                    cubes = (
                        (endpoints["x"][x + 1] - endpoints["x"][x])
                        * (endpoints["y"][y + 1] - endpoints["y"][y])
                        * (endpoints["z"][z + 1] - endpoints["z"][z])
                    )
                    count += cubes

    return count


if __name__ == "__main__":
    commands = read_input_part_2("example.txt")
    print(part_2(commands))
