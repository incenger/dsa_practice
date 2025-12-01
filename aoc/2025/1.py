SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

CLOCK_SIZE = 100
INIT_POS = 50


def read_input(file):
    ops = []
    with open(file, "r") as f:
        for line in f.readlines():
            ops.append((line[0], int(line[1:])))
    return ops


def part_1(file):
    ops = read_input(file)
    cur_pos = INIT_POS
    password = 0
    for dir, step in ops:
        if dir == 'L':
            step *= -1
        cur_pos = (cur_pos + step) % CLOCK_SIZE
        if cur_pos == 0:
            password += 1
    print(f"Part 1: {password}")


def part_2(file):
    ops = read_input(file)
    cur_pos = INIT_POS
    password = 0
    for dir, step in ops:
        password += step // CLOCK_SIZE
        step %= CLOCK_SIZE

        if dir == 'L':
            step *= -1
        target = cur_pos + step
        if target >= CLOCK_SIZE or target * cur_pos < 0 or target == 0:
            password += 1

        cur_pos = target % CLOCK_SIZE
    print(f"Part 2: {password}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
