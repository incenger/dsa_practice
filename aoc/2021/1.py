import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()


def part_1_2(depths, window_size):
    diff = depths[window_size:] - depths[:-window_size]
    return sum([1 for x in diff if x > 0])


if __name__ == "__main__":
    depths = np.array([int(line.strip()) for line in lines])
    print(part_1_2(depths))
