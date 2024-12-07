"""
time python3 7.py
python3 7.py  4.07s user 0.17s system 91% cpu 4.628 total
"""

import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    equations = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            test_value, numbers = line.split(":")
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            equations.append((test_value, numbers))
    return equations


def part_1(file):
    equations = read_input(file)

    NUM_OPS = 2

    def check(test_value, numbers):
        n = len(numbers)
        queue = collections.deque([(numbers[0], 0)])
        while queue:
            value, idx = queue.popleft()
            for op_idx in range(NUM_OPS):
                if op_idx == 0:
                    new_value = value + numbers[idx + 1]
                else:
                    new_value = value * numbers[idx + 1]

                if new_value == test_value and idx == n - 2:
                    return True

                if new_value <= test_value and idx < n - 2:
                    queue.append((new_value, idx + 1))
        return False

    answer = 0
    for test_value, numbers in equations:
        if check(test_value, numbers):
            answer += test_value
    print("ANSWER:", answer)


def part_2(file):
    equations = read_input(file)

    NUM_OPS = 3

    def check(test_value, numbers):
        n = len(numbers)
        queue = collections.deque([(numbers[0], 0)])
        while queue:
            value, idx = queue.popleft()
            for op_idx in range(NUM_OPS):
                if op_idx == 0:
                    new_value = value + numbers[idx + 1]
                elif op_idx == 1:
                    new_value = value * numbers[idx + 1]
                else:
                    new_value = int(f"{value}{numbers[idx+1]}")

                if new_value == test_value and idx == n - 2:
                    return True

                if new_value <= test_value and idx < n - 2:
                    queue.append((new_value, idx + 1))
        return False

    answer = 0
    for test_value, numbers in equations:
        if check(test_value, numbers):
            answer += test_value
    print("ANSWER:", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
