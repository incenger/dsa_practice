def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    points = set()
    folds = []
    for line in lines:
        if "," in line:
            point = tuple(map(int, line.split(",")))
            points.add(point)
        elif "fold" in line:
            fold = line.split()[2]
            direction, position = fold.split("=")
            folds.append((direction, int(position)))
    return points, folds


def fold(points, position, direction):
    """ """
    new_points = set()
    for x, y in points:
        if direction == "y":
            if y > position:
                new_point = (x, 2 * position - y)
            else:
                new_point = (x, y)
            new_points.add(new_point)
        else:
            if x > position:
                new_point = (2 * position - x, y)
            else:
                new_point = (x, y)
            new_points.add(new_point)

    return new_points


def part_1(points, folds):
    return fold(points, folds[0][1], folds[0][0])


def part_2(points, folds):
    for f in folds:
        points = fold(points, f[1], f[0])
    return points


if __name__ == "__main__":
    points, folds = read_input("input.txt")
    new_points = part_2(points, folds)
    max_x = max([p[0] for p in new_points]) + 1
    max_y = max([p[1] for p in new_points]) + 1

    mark = [["."] * max_x for _ in range(max_y)]

    for x, y in new_points:
        mark[y][x] = "#"

    for line in mark:
        print("".join(line))
