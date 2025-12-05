import re

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

RANGE_REGEX = re.compile(r"(\d+)-(\d+)", re.IGNORECASE)


def read_input(file):
    ranges = []
    queries = []
    is_range = True
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                is_range = False
            elif is_range:
                ranges.append(tuple(map(int, RANGE_REGEX.findall(line)[0])))
            else:
                queries.append(int(line))

    return ranges, queries


def part_1(file):
    ranges, queries = read_input(file)
    answer = 0
    for query in queries:
        if any(begin <= query <= end for begin, end in ranges):
            answer += 1
    print(f"Part 1: {answer}")


def part_2(file):
    ranges = read_input(file)[0]
    ranges.sort()
    answer = 0
    cur_range = ranges[0]

    for i in range(1, len(ranges)):
        begin, end = ranges[i]
        if begin > cur_range[1]:
            # No overlapping, we start a new range
            answer += cur_range[1] - cur_range[0] + 1
            cur_range = ranges[i]
        else:
            cur_range = (min(cur_range[0], begin), max(cur_range[1], end))
    answer += cur_range[1] - cur_range[0] + 1

    print(f"Part 2: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
