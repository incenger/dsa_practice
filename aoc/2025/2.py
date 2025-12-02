import re

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

ID_REGEX = re.compile(r"(\d+)-(\d+)", re.IGNORECASE)


def read_input(file):
    id_ranges = []
    with open(file, "r") as f:
        for line in f.readlines():
            matches = ID_REGEX.findall(line)
            for match in matches:
                id_ranges.append((int(match[0]), int(match[1])))
    return id_ranges


def is_invalid_id(id: int, num_digits: int, block_size: int):
    if block_size == 0:
        return False

    if num_digits % block_size != 0:
        return False

    mask = 10**block_size
    block_value = id % mask
    while id:
        if id % mask != block_value:
            return False
        id //= mask
    return True


def sum_invalid_ids(begin, end, part):
    invalid_sum = 0
    for id in range(begin, end + 1):
        num_digits = len(str(id))

        if part == 1 and is_invalid_id(
                id, num_digits, block_size=num_digits // 2):
            invalid_sum += id

        if part == 2:
            for block_size in range(1, num_digits // 2):
                if is_invalid_id(id, num_digits, block_size):
                    invalid_sum += id
                    break
    return invalid_sum


def part_1(file):
    id_ranges = read_input(file)
    res = 0
    for begin, end in id_ranges:
        for id in range(begin, end + 1):
            num_digits = len(str(id))
            if num_digits % 2 == 0 and is_invalid_id(
                    id, num_digits, block_size=num_digits // 2):
                res += id
    print(f"Part 1: {res}")


def part_2(file):
    id_ranges = read_input(file)
    res = 0
    for begin, end in id_ranges:
        for id in range(begin, end + 1):
            num_digits = len(str(id))
            for block_size in range(1, num_digits // 2 + 1):
                if is_invalid_id(id, num_digits, block_size):
                    res += id
                    break
    print(f"Part 1: {res}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
