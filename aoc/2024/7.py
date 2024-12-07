"""
time python3 7.py
python3 7.py  26.50s user 0.65s system 97% cpu 27.931 total
"""
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
    answer = 0
    for test_value, numbers in equations:
        n = len(numbers)
        for mask in range(2**(n - 1)):
            value = numbers[0]
            for i in range(n - 1):
                if mask % 2 == 0:
                    value *= numbers[i + 1]
                else:
                    value += numbers[i + 1]
                mask //= 2
                if value > test_value:
                    break
            if value == test_value:
                answer += test_value
                break
    print("ANSWER:", answer)


def part_2(file):
    equations = read_input(file)
    answer = 0
    for test_value, numbers in equations:
        n = len(numbers)
        for mask in range(3**(n - 1)):
            value = numbers[0]
            for i in range(n - 1):
                if mask % 3 == 0:
                    value *= numbers[i + 1]
                elif mask % 3 == 1:
                    value += numbers[i + 1]
                else:
                    value = int(f"{value}{numbers[i+1]}")
                mask //= 3
                if value > test_value:
                    break
            if value == test_value:
                answer += test_value
                break
    print("ANSWER:", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
