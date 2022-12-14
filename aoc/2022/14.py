def part_1():
    rock_paths = []
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            endpoints = line.split("->")
            endpoints = [tuple(map(int, endpoint.split(","))) for endpoint in endpoints]
            rock_paths.append(endpoints)

    blocked = set()

    for rock_path in rock_paths:
        for i in range(len(rock_path) - 1):
            x0, y0 = rock_path[i]
            x1, y1 = rock_path[i + 1]
            for x in range(min(x0, x1), max(x0, x1) + 1):
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    blocked.add((x, y))

    abyss = max(y for _, y in blocked) + 1

    START_POSITION = (500, 0)
    cur_position = START_POSITION

    dirs = (0, -1, 1)
    sand_rest_cnt = 0
    while True:

        cur_x, cur_y = cur_position

        if cur_y >= abyss:
            break

        for dx in dirs:
            next_position = (cur_x + dx, cur_y + 1)

            if next_position in blocked:
                continue

            cur_position = next_position
            break
        else:
            blocked.add(cur_position)
            sand_rest_cnt += 1
            cur_position = START_POSITION

    print("Part 1:", sand_rest_cnt)


def part_2():
    rock_paths = []
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            endpoints = line.split("->")
            endpoints = [tuple(map(int, endpoint.split(","))) for endpoint in endpoints]
            rock_paths.append(endpoints)

    blocked = set()

    for rock_path in rock_paths:
        for i in range(len(rock_path) - 1):
            x0, y0 = rock_path[i]
            x1, y1 = rock_path[i + 1]
            for x in range(min(x0, x1), max(x0, x1) + 1):
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    blocked.add((x, y))

    floor_y = max(y for _, y in blocked) + 2

    START_POSITION = (500, 0)
    cur_position = START_POSITION

    dirs = (0, -1, 1)
    sand_rest_cnt = 0
    while True:

        cur_x, cur_y = cur_position

        for dx in dirs:
            next_position = (cur_x + dx, cur_y + 1)

            if next_position in blocked:
                continue

            if next_position[1] >= floor_y:
                continue

            cur_position = next_position
            break
        else:
            if cur_position == START_POSITION:
                break

            sand_rest_cnt += 1

            blocked.add(cur_position)
            cur_position = START_POSITION

    print("Part 2:", sand_rest_cnt)


if __name__ == "__main__":
    part_1()
    part_2()
