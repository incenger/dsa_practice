"""
time python3 11.py
python3 11.py  0.10s user 0.02s system 91% cpu 0.139 total
"""
import functools

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    with open(file, "r") as f:
        return list(map(int, f.readline().split()))


@functools.cache
def count_stones(num, blinks):
    """Number of stones created from this one (including itself) after blinks."""
    if blinks == 0:
        return 1
    if num == 0:
        return count_stones(1, blinks - 1)
    digits = str(num)
    if len(digits) % 2 == 1:
        return count_stones(num * 2024, blinks - 1)
    else:
        left = int(digits[:len(digits) // 2])
        right = int(digits[len(digits) // 2:])
        return count_stones(left, blinks - 1) + count_stones(right, blinks - 1)


def part_1(file):
    stones = read_input(file)
    BLINKS = 25
    answer = 0
    for stone in stones:
        answer += count_stones(stone, BLINKS)
    print("ANSWER:", answer)


def part_2(file):

    stones = read_input(file)
    BLINKS = 75
    answer = 0
    for stone in stones:
        answer += count_stones(stone, BLINKS)
    print("ANSWER:", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
