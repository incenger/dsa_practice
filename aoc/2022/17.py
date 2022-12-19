NUM_ROCK_TYPES = 5
NEW_ROCK_VERTICAL_SPACE = 3
CHAMBER_WIDTH = 7
FLOOR = ["#"] * CHAMBER_WIDTH


def get_rock(type, height):
    # Get a rock with bottom at height
    if type == 0:
        # ooo
        return set([(x, height) for x in range(2, 6)])
    elif type == 1:
        #  o
        # ooo
        #  o
        return set(
            [(x, height + 1) for x in range(2, 5)] + [(3, height), (3, height + 2)]
        )
    elif type == 2:
        #   o
        #   o
        # ooo
        return set(
            [(x, height) for x in range(2, 5)]
            + [(4, y) for y in range(height + 1, height + 3)]
        )
    elif type == 3:
        # o
        # o
        # o
        # o
        return set([(2, y) for y in range(height, height + 4)])
    elif type == 4:
        # oo
        # oo
        return set([(x, y) for x in range(2, 4) for y in range(height, height + 2)])
    else:
        raise ValueError("Invalid type", type)


def shift_left(rock):
    return set([(x - 1, y) for x, y in rock])


def shift_right(rock):
    return set([(x + 1, y) for x, y in rock])


def fall_down(rock):
    return set([(x, y - 1) for x, y in rock])


def is_valid(rock, chamber):
    # Check if the current rock position is valid
    for x, y in rock:

        if x >= CHAMBER_WIDTH or x < 0:
            return False

        if y < 0:
            # Touches the floor
            return False

        if y >= len(chamber):
            continue

        if chamber[y][x] != ".":
            return False

    return True


def print_chamber(chamber):
    for i, row in reversed(list(enumerate(chamber))):
        print(f"{str(i).zfill(4)}: {''.join(row)}")


def part_1(input_file):
    with open(input_file, "r") as f:
        pattern = f.readline().strip()

    chamber = [["#"] * CHAMBER_WIDTH]  # The floor
    chamber_height = 0

    rock_cnt = 1
    target_rock_cnt = 2022
    pattern_idx = 0

    while rock_cnt <= target_rock_cnt:
        # Run the simulation
        rock_type = (rock_cnt - 1) % NUM_ROCK_TYPES
        rock = get_rock(rock_type, chamber_height + NEW_ROCK_VERTICAL_SPACE + 1)

        while True:
            move = pattern[pattern_idx]
            pattern_idx = (pattern_idx + 1) % len(pattern)

            rock_next_pos = shift_right(rock) if move == ">" else shift_left(rock)

            if is_valid(rock_next_pos, chamber):
                rock = rock_next_pos

            rock_next_pos = fall_down(rock)
            if not is_valid(rock_next_pos, chamber):
                break
            else:
                rock = rock_next_pos

        chamber_height = max(chamber_height, max(y for _, y in rock))
        # Increase chamber if needed
        while len(chamber) < chamber_height + 1:
            chamber.append(["."] * CHAMBER_WIDTH)
        # Update chamber info
        for x, y in rock:
            chamber[y][x] = "#"

        rock_cnt += 1

    print_chamber(chamber)
    print("Part 1", chamber_height)


def get_pattern(chamber, pattern_window=30):
    return "".join(["".join(row) for row in chamber[-pattern_window:]])


def part_2(input_file):
    """We keep track of a window of chamber and search for repeated patterns.

    The pattern window is just a herusitic, just big enough so it could search for something meaningful.

    """
    with open(input_file, "r") as f:
        pattern = f.readline().strip()

    chamber = [FLOOR]  # The floor
    chamber_height = 0

    rock_cnt = 1
    target_rock_cnt = 1000000000000
    pattern_idx = 0
    repeated_height = -1

    seen_chamber_pattern = {}

    while rock_cnt <= target_rock_cnt:
        # Run the simulation
        rock_type = (rock_cnt - 1) % NUM_ROCK_TYPES
        rock = get_rock(rock_type, chamber_height + NEW_ROCK_VERTICAL_SPACE + 1)

        while True:
            move = pattern[pattern_idx]
            pattern_idx = (pattern_idx + 1) % len(pattern)

            rock_next_pos = shift_right(rock) if move == ">" else shift_left(rock)

            if is_valid(rock_next_pos, chamber):
                rock = rock_next_pos

            rock_next_pos = fall_down(rock)
            if not is_valid(rock_next_pos, chamber):
                break
            else:
                rock = rock_next_pos

        chamber_height = max(chamber_height, max(y for _, y in rock))
        # Increase chamber if needed
        while len(chamber) < chamber_height + 1:
            chamber.append(["."] * CHAMBER_WIDTH)

        # Update chamber info
        for x, y in rock:
            chamber[y][x] = "#"

        chamber_pattern = (rock_type, pattern_idx, get_pattern(chamber))

        if repeated_height == -1 and chamber_pattern in seen_chamber_pattern:

            prev_rock_cnt, prev_height = seen_chamber_pattern[chamber_pattern]
            rock_cnt_diff = rock_cnt - prev_rock_cnt
            height_diff = chamber_height - prev_height

            n_repeated = (target_rock_cnt - prev_rock_cnt) // rock_cnt_diff
            rock_cnt = prev_rock_cnt + n_repeated * rock_cnt_diff
            repeated_height = (n_repeated - 1) * height_diff

        else:
            seen_chamber_pattern[chamber_pattern] = (rock_cnt, chamber_height)

        rock_cnt += 1

    assert repeated_height != -1
    print("Part 2", chamber_height + repeated_height)


if __name__ == "__main__":
    # part_1("input.txt")
    part_2("input.txt")
