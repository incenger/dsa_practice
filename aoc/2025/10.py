import math
import re

from scipy.optimize import linprog

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

INPUT_PATTERN = r"\[(.*?)\].*?((?:\(.*?\)\s*)+).*?\{(.*?)\}"
BUTTON_PATTERN = r'\((.*?)\)'


def read_input(file):
    machines = []
    with open(file, "r") as f:
        for line in f.readlines():
            match = re.search(INPUT_PATTERN, line)
            if match:
                # Convert the current state to binary representation
                goal_str = match.group(1).strip()
                goal_str_binary = "".join('1' if ch == '#' else '0'
                                          for ch in reversed(goal_str))
                num_lights = len(goal_str)
                goal_state = int(goal_str_binary, base=2)

                button_str = match.group(2)
                buttons = re.findall(BUTTON_PATTERN, button_str)
                activate_lights = []
                for button in buttons:
                    activate_lights.append(
                        [int(x.strip()) for x in button.split(",")])

                joltage_str = match.group(3)
                joltages = [int(x) for x in joltage_str.split(",")]
                machines.append(
                    (num_lights, goal_state, activate_lights, joltages))
    return machines


def part_1(file):
    machines = read_input(file)
    answer = 0
    for num_lights, goal_state, buttons, _ in machines:
        min_num_press = num_lights + 1
        num_buttons = len(buttons)
        for mask in range(1 << num_buttons):
            current_state = 0
            press_count = 0
            for i in range(num_buttons):
                if mask & (1 << i):
                    press_count += 1
                    for activate_light in buttons[i]:
                        current_state ^= (1 << activate_light)
            if current_state == goal_state:
                min_num_press = min(min_num_press, press_count)

        answer += min_num_press
    print(f"Part 1: {answer}")


def to_matrix(buttons, num_lights):
    matrix = [[0] * len(buttons) for _ in range(num_lights)]
    for idx, activate_lights in enumerate(buttons):
        for light in activate_lights:
            matrix[light][idx] += 1
    return matrix


def part_2(file):
    # Solve the linear optimization
    # (num_lights, num_buttons) * (num_buttons, 1) =  (num_lights, 1)
    # Bx = C
    machines = read_input(file)
    answer = 0
    for num_lights, _, buttons, counter in machines:
        matrix = to_matrix(buttons, num_lights)
        res = linprog(c=[1] * len(buttons),
                      A_eq=matrix,
                      b_eq=counter,
                      integrality=1)
        answer += int(sum(res.x))
    print(f"Part 1: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
