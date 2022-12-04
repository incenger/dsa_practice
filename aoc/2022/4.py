def contains(interval_a, interval_b):
    """Whether `interval_a` fully contains `interval_b`"""
    xmin_a, xmax_a = interval_a
    xmin_b, xmax_b = interval_b
    return xmin_a <= xmin_b and xmax_b <= xmax_a


def overlaps(interval_a, interval_b):
    """Whether `interval_a` overlaps with `interval_b`"""
    xmin_a, xmax_a = interval_a
    xmin_b, xmax_b = interval_b
    return xmin_b <= xmax_a <= xmax_b or xmin_a <= xmax_b <= xmax_a


def parse_interval(line):
    first_interval, second_interval = line.split(",")
    first_interval = list(map(int, first_interval.split("-")))
    second_interval = list(map(int, second_interval.split("-")))
    return first_interval, second_interval


def part_1_2():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    contain_count = 0
    overlap_count = 0
    for line in lines:
        first_interval, second_interval = parse_interval(line)
        if contains(first_interval, second_interval) or contains(
            second_interval, first_interval
        ):
            contain_count += 1

        if overlaps(first_interval, second_interval):
            overlap_count += 1
    print("Part 1 answer:", contain_count)
    print("Part 2 answer:", overlap_count)


if __name__ == "__main__":
    part_1_2()
