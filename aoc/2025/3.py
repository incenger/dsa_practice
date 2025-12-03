import collections
import functools

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    banks = []
    with open(file, "r") as f:
        for line in f.readlines():
            digits = tuple(map(int, line.strip()))
            banks.append(digits)
    return banks


def max_joltage(bank, max_choice):

    @functools.cache
    def find_max(idx, remain_choice):
        if remain_choice == 0:
            return 0
        if idx == len(bank):
            return 0 if remain_choice == 0 else float('-inf')

        exp = 10**(remain_choice - 1)
        return max(bank[idx] * exp + find_max(idx + 1, remain_choice - 1),
                   find_max(idx + 1, remain_choice))

    return find_max(0, max_choice)


def part_1(file):
    banks = read_input(file)
    answer = 0
    for bank in banks:
        m = max_joltage(bank, max_choice=2)
        answer += m
    print(f"Part 1: {answer}")


def part_2(file):
    banks = read_input(file)
    answer = 0
    for bank in banks:
        m = max_joltage(bank, max_choice=12)
        answer += m
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
