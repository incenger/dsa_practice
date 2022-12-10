import bisect


def part_1():
    with open("input.txt", "r") as f:
        commands = [line.strip() for line in f.readlines()]

    CYCLE_OF_INTEREST = [20, 60, 100, 140, 180, 220]

    cycle = 0
    register_value = [(cycle, 1)]
    for command in commands:
        command = command.split()
        if len(command) == 1:
            cycle += 1
        elif len(command) == 2:
            cycle += 2
            add_value = int(command[1])
            last_value = register_value[-1][1]
            register_value.append((cycle, last_value + add_value))

    total_signal_strength = 0
    for c in CYCLE_OF_INTEREST:
        # Find the first cycle that is smaller than this one
        idx = bisect.bisect(register_value, (c, 0)) - 1
        value = register_value[idx][1]
        signal_strength = c * value
        total_signal_strength += signal_strength

    print("Part 1", total_signal_strength)


def part_2():
    with open("input.txt", "r") as f:
        commands = [line.strip() for line in f.readlines()]

    cycle = 0
    register_value = [(cycle, 0)]
    for command in commands:
        command = command.split()
        if len(command) == 1:
            cycle += 1
        elif len(command) == 2:
            cycle += 2
            add_value = int(command[1])
            last_value = register_value[-1][1]
            register_value.append((cycle, last_value + add_value))

    m, n = 6, 40
    CRT_SCREEN = [[" "] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            current_cycle = n * i + j
            idx = bisect.bisect(register_value, (current_cycle, (float("inf")))) - 1
            position = register_value[idx][1]
            if position <= j <= position + 2:
                CRT_SCREEN[i][j] = "\u2588"

    print("Part 2")
    for row in CRT_SCREEN:
        print("".join(row))


if __name__ == "__main__":
    part_1()
    part_2()
