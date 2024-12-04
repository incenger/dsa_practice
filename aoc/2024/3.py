import re

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

def read_input(file):
    with open(file, "r") as f:
        memory_lines = [line.strip() for line in f.readlines()]
    return memory_lines


def part_1(file):
    memory_lines = read_input(file)
    mul_pattern = r"mul\((\d+),(\d+)\)"
    result = 0
    for memory in memory_lines:
        for num_1, num_2 in re.findall(mul_pattern, memory):
            result += int(num_1) * int(num_2)
    print(f"ANSWER: {result}")

def part_2(file):
    memory_lines = read_input(file)
    mul_pattern = r"mul\((\d+),(\d+)\)|(don't\(\))|(do())"
    result = 0
    enable = True
    for memory in memory_lines:
        for match in re.findall(mul_pattern, memory):
            if match[2]:
                enable = False
            if match[3]:
                enable = True
            if match[0] and match[1] and enable:
                result += int(match[0]) * int(match[1])
    print(f"ANSWER: {result}")



if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
