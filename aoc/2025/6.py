import math

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    problem = []
    with open(file, "r") as f:
        for line in f.readlines():
            problem.append(line.strip("\n"))
    return problem


def compute(problem, order):
    M, N = len(problem), len(problem[0])

    splits = []
    for col in range(N):
        if all(problem[row][col] == " " for row in range(M)):
            splits.append(col)
    splits.append(N)

    res = 0
    prev_split = -1
    for split in splits:
        if order == "row":
            numbers = [
                problem[row][prev_split + 1:split] for row in range(M - 1)
            ]
        else:
            numbers = [
                "".join(problem[row][col] for row in range(M - 1))
                for col in range(prev_split + 1, split)
            ]

        op = problem[-1][prev_split + 1]
        if op == '+':
            res += sum(map(int, numbers))
        else:
            res += math.prod(map(int, numbers))

        prev_split = split
    return res


def part_1(file):
    problem = read_input(file)
    answer = compute(problem, order="row")

    print(f"Part 1: {answer}")


def part_2(file):
    problem = read_input(file)
    answer = compute(problem, order="col")
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
