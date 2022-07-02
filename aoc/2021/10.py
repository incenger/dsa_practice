from collections import deque


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()

    lines = [l.strip() for l in lines]
    return lines


MATCH = {
    "]": "[",
    ")": "(",
    ">": "<",
    "}": "{",
}

CHECK_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}

COMPLETE_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def part_1(lines):

    errors = []

    for line in lines:
        stack = deque()

        for c in line:
            top = stack[-1] if len(stack) else ""
            if c in MATCH:
                if top != MATCH[c]:
                    errors.append(c)
                    break
                else:
                    stack.pop()
            else:
                stack.append(c)
    print(errors)
    return sum((CHECK_SCORE[e] for e in errors))


def part_2(lines):

    scores = []
    REVERSED_MATCH = {v: k for k, v in MATCH.items()}

    for line in lines:
        stack = deque()

        for c in line:
            top = stack[-1] if len(stack) else ""
            if c in MATCH:
                if top != MATCH[c]:
                    break
                else:
                    stack.pop()
            else:
                stack.append(c)
        else:
            # Incomplete line
            score = 0
            while len(stack):
                score = (score * 5) + COMPLETE_SCORE[REVERSED_MATCH[stack[-1]]]
                stack.pop()

            scores.append(score)
    scores.sort()
    mid_value = scores[len(scores) // 2]
    return mid_value


if __name__ == "__main__":
    lines = read_input("./input.txt")
    print(part_2(lines))
