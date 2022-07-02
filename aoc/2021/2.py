import numpy as np


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [line.split() for line in lines]
    commands = [(direction, int(step)) for direction, step in lines]
    return commands


def part_1(commands):
    pos = np.array([0, 0])

    for direction, step in commands:
        if direction == "forward":
            pos = pos + np.array([0, step])
        elif direction == "up":
            pos = pos - np.array([step, 0])
        else:
            pos = pos + np.array([step, 0])
    return pos[0] * pos[1]

def part_2(commands):
    pos = np.array([0, 0])
    aim = 0

    for direction, step in commands:
        if direction == "forward":
            pos = pos + np.array([0, step])
            pos = pos + np.array([aim*step, 0])
        elif direction == "up":
            aim -= step
        else:
            aim += step
    return pos[0] * pos[1]

if __name__ == "__main__":
    commands = read_input("input.txt")
    print(part_2(commands))
