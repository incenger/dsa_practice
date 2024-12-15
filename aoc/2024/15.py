"""
time python3 15.py
python3 15.py  0.03s user 0.02s system 81% cpu 0.061 total
"""
SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIR_MAP = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}


def read_input(file):
    warehouse_map = []
    moves = []
    with open(file, "r") as f:
        is_map = True
        for line in f.readlines():
            line = line.strip()
            if not line:
                is_map = False
            elif is_map:
                warehouse_map.append(list(line))
            else:
                moves.extend((DIR_MAP[move] for move in line))
    return warehouse_map, moves


def find_robot_location(warehouse_map):
    M, N = len(warehouse_map), len(warehouse_map[0])
    # Find position of the robot '@'
    for row in range(M):
        for col in range(N):
            if warehouse_map[row][col] == '@':
                return (row, col)
    return None


def part_1(file):
    warehouse_map, moves = read_input(file)
    M, N = len(warehouse_map), len(warehouse_map[0])

    def push_box(box_row, box_col, drow, dcol):
        steps = 0
        while warehouse_map[box_row + steps * drow][box_col +
                                                    steps * dcol] == 'O':
            steps += 1

        # Just need to move the first box to the new position
        new_box_row = box_row + drow * steps
        new_box_col = box_col + dcol * steps
        if warehouse_map[new_box_row][new_box_col] == '.':
            warehouse_map[box_row][box_col] = '.'
            warehouse_map[new_box_row][new_box_col] = 'O'
            return True
        return False

    robot_row, robot_col = find_robot_location(warehouse_map)
    warehouse_map[robot_row][robot_col] = '.'

    for drow, dcol in moves:
        next_row, next_col = robot_row + drow, robot_col + dcol

        if warehouse_map[next_row][next_col] == '#':
            continue

        if warehouse_map[next_row][next_col] == '.':
            robot_row, robot_col = next_row, next_col

        if warehouse_map[next_row][next_col] == 'O':
            if push_box(next_row, next_col, drow, dcol):
                robot_row, robot_col = next_row, next_col

    answer = 0
    for row in range(M):
        for col in range(N):
            if warehouse_map[row][col] == 'O':
                answer += 100 * row + col
    print("ANSWER", answer)


def transform_map(warehouse_map):
    new_map = []
    for row in warehouse_map:
        new_row = []
        for ch in row:
            if ch == '#':
                new_row.extend(['#', '#'])
            elif ch == 'O':
                new_row.extend(['[', ']'])
            elif ch == '.':
                new_row.extend(['.', '.'])
            else:
                new_row.extend(['@', '.'])
        new_map.append(new_row)
    return new_map


def push_horizontal(warehouse_map, box_row, box_col, dcol):
    steps = 0
    while warehouse_map[box_row][box_col + steps * dcol] in "[]":
        steps += 1

    if warehouse_map[box_row][box_col + dcol * steps] != '.':
        return False

    for step in range(steps, 0, -1):
        cur_col = box_col + dcol * step
        warehouse_map[box_row][cur_col] = warehouse_map[box_row][cur_col -
                                                                 dcol]
    warehouse_map[box_row][box_col] = '.'
    return True


def can_push_vertical(warehouse_map, box_row, box_col, drow):
    push_locations = [(box_row, box_col)]
    if warehouse_map[box_row][box_col] == '[':
        push_locations.append((box_row, box_col + 1))
    else:
        push_locations.append((box_row, box_col - 1))

    for row, col in push_locations:
        next_row = row + drow
        if warehouse_map[next_row][col] == '#':
            return False
        if warehouse_map[next_row][col] != '.' and not can_push_vertical(
                warehouse_map, next_row, col, drow):
            return False

    return True


def push_vertical(warehouse_map, box_row, box_col, drow):
    push_locations = [(box_row, box_col)]
    if warehouse_map[box_row][box_col] == '[':
        push_locations.append((box_row, box_col + 1))
    else:
        push_locations.append((box_row, box_col - 1))

    for row, col in push_locations:
        next_row = row + drow
        if warehouse_map[next_row][col] == '.':
            warehouse_map[next_row][col] = warehouse_map[row][col]
            warehouse_map[row][col] = '.'
        else:
            push_vertical(warehouse_map, next_row, col, drow)
            warehouse_map[next_row][col] = warehouse_map[row][col]
            warehouse_map[row][col] = '.'


def debug(warehouse_map, robot_row, robot_col):
    warehouse_map[robot_row][robot_col] = '@'
    for row in warehouse_map:
        print("".join(row))
    warehouse_map[robot_row][robot_col] = '.'


def part_2(file):
    warehouse_map, moves = read_input(file)
    warehouse_map = transform_map(warehouse_map)
    M, N = len(warehouse_map), len(warehouse_map[0])

    robot_row, robot_col = find_robot_location(warehouse_map)
    warehouse_map[robot_row][robot_col] = '.'

    for drow, dcol in moves:
        next_row, next_col = robot_row + drow, robot_col + dcol

        if warehouse_map[next_row][next_col] == '#':
            continue

        if warehouse_map[next_row][next_col] == '.':
            robot_row, robot_col = next_row, next_col

        if warehouse_map[next_row][next_col] in '[]':
            if drow == 0 and push_horizontal(warehouse_map, next_row, next_col,
                                             dcol):
                robot_row, robot_col = next_row, next_col
            elif dcol == 0 and can_push_vertical(warehouse_map, next_row,
                                                 next_col, drow):
                push_vertical(warehouse_map, next_row, next_col, drow)
                robot_row, robot_col = next_row, next_col

    answer = 0
    for row in range(M):
        for col in range(N):
            if warehouse_map[row][col] == '[':
                answer += 100 * row + col
    print("ANSWER", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
