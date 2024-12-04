from collections import Counter

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    list_1, list_2 = [], []
    with open(file, "r") as f:
        for line in f.readlines():
            num_1, num_2 = map(int, line.split())
            list_1.append(num_1)
            list_2.append(num_2)

    return list_1, list_2


def part_1(file):
    list_1, list_2 = read_input(file)
    list_1.sort()
    list_2.sort()
    total_dist = 0
    for num_1, num_2 in zip(list_1, list_2):
        total_dist += abs(num_1 - num_2)
    print(f"ANSWER: {total_dist}")


def part_2(file):
    list_1, list_2 = read_input(file)
    counter_2 = Counter(list_2)
    score = 0
    for num_1 in list_1:
        score += num_1 * counter_2[num_1]
    print(f"ANSWER: {score}")


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_2(SAMPLE_FILE)
