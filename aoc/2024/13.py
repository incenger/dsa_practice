"""
time python3 13.py
python3 13.py  0.03s user 0.03s system 74% cpu 0.070 total
"""
import re

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

COST_A = 3
COST_B = 1
CONVERSION_ERROR = 10000000000000


def read_input(file):
    claw_machines = []
    button_regex = re.compile(r"(X|Y)\+(\d+)")
    prize_regex = re.compile(r"(X|Y)=(\d+)")
    with open(file, "r") as f:
        lines = f.readlines()
        for idx in range(0, len(lines), 4):
            button_a = lines[idx].strip()
            (_, a_x), (_, a_y) = button_regex.findall(button_a)
            button_b = lines[idx + 1].strip()
            (_, b_x), (_, b_y) = button_regex.findall(button_b)
            prize = lines[idx + 2].strip()
            (_, p_x), (_, p_y) = prize_regex.findall(prize)
            claw_machines.append((
                (int(a_x), int(a_y)),
                (int(b_x), int(b_y)),
                (int(p_x), int(p_y)),
            ))
    return claw_machines


def part_1(file):
    # A_x * a + B_x * b == P_x
    # A_y * a + B_y * b == P_y
    claw_machines = read_input(file)
    answer = 0
    for (a_x, a_y), (b_x, b_y), (p_x, p_y) in claw_machines:
        D = a_x * b_y - a_y * b_x
        D_a = p_x * b_y - p_y * b_x
        D_b = p_y * a_x - a_y * p_x
        if D != 0 and D_a % D == 0 and D_b % D == 0:
            min_tokens = (D_a // D) * COST_A + (D_b // D) * COST_B
            answer += min_tokens
    print("ANSWER", answer)


def part_2(file):
    claw_machines = read_input(file)
    answer = 0
    for (a_x, a_y), (b_x, b_y), (p_x, p_y) in claw_machines:
        p_x += CONVERSION_ERROR
        p_y += CONVERSION_ERROR
        D = a_x * b_y - a_y * b_x
        D_a = p_x * b_y - p_y * b_x
        D_b = p_y * a_x - a_y * p_x
        if D != 0 and D_a % D == 0 and D_b % D == 0:
            min_tokens = (D_a // D) * COST_A + (D_b // D) * COST_B
            answer += min_tokens
    print("ANSWER", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
