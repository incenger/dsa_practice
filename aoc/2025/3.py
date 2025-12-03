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
    dp = [0] * (max_choice + 1)
    for digit in bank:
        new_dp = dp
        for j in range(max_choice - 1, -1, -1):
            new_dp[j + 1] = max(new_dp[j + 1], dp[j] * 10 + digit)
        dp = new_dp
    return dp[max_choice]


def part_1(file):
    banks = read_input(file)
    answer = 0
    for bank in banks:
        answer += max_joltage(bank, max_choice=2)
    print(f"Part 1: {answer}")


def part_2(file):
    banks = read_input(file)
    answer = 0
    for bank in banks:
        answer += max_joltage(bank, max_choice=12)
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
