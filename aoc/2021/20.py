"""
Better algorithm:

For each enhance interation
- Pad the input with 2 with appropriate value
- Initialize the result with appropriate value
- Fill the result
"""
from copy import deepcopy


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    img_enhance = lines[0]

    img = []
    for line in lines[2:]:
        img.append(list(line.strip()))

    return img_enhance, img


DIRR = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
DIRC = [-1, 0, 1, -1, 0, 1, -1, 0, 1]


def enhance_img(img, algo, padding):
    m = len(img)
    n = len(img[0])

    # Add padding to A
    result = deepcopy(img)

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            value = "".join(
                [
                    "1" if img[i + dr][j + dc] == "#" else "0"
                    for dr, dc in zip(DIRR, DIRC)
                ]
            )
            index = int(value, 2)
            new_value = algo[index]
            result[i][j] = new_value

    # Update the padding value
    for i in range(m):
        result[i][0] = result[i][-1] = padding
    for j in range(n):
        result[0][j] = result[-1][j] = padding

    return result


def part_1(algo, grid):
    offset = 200
    m = len(grid)
    n = len(grid[0])
    padded_grid = [["."] * (offset * 2 + n) for _ in range(offset * 2 + m)]

    # Need to fix the padding value
    # It jumps between the first and last value depends on the algo
    # If algo[0] == '.' -> It remains dots all the time
    # If algo[0] == '#' -> It juggles between . and #
    if algo[0] == ".":
        paddings = [".", "."]
    else:
        paddings = ["#", "."]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                padded_grid[i + offset][j + offset] = "#"

    result = padded_grid

    for time in range(50):
        result = enhance_img(result, algo, paddings[time % 2])

    count = sum([1 if c == "#" else 0 for line in result for c in line])

    return count


if __name__ == "__main__":
    img_enhance, img = read_input("input.txt")
    count = part_1(img_enhance, img)
    print(count)
