def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    region = [l.strip() for l in lines]
    return region


def next_east_cell(r, c, m, n):
    """
    r,c: current row and column
    m,n: height and width of the region
    """
    c = (c + 1) % n
    return (r, c)


def next_south_cell(r, c, m, n):
    """
    r,c: current row and column
    m,n: height and width of the region
    """
    r = (r + 1) % m
    return (r, c)


def part_1(region):
    m, n = len(region), len(region[0])
    east_facing = set()
    south_facing = set()

    for r, row in enumerate(region):
        for c, cell in enumerate(row):
            if cell == "v":
                south_facing.add((r, c))
            elif cell == ">":
                east_facing.add((r, c))

    step = 0
    while True:
        step += 1

        new_east_facing = set()
        new_south_facing = set()
        can_move = False
        for r, c in east_facing:
            nr, nc = next_east_cell(r, c, m, n)
            if (nr, nc) not in east_facing and (nr, nc) not in south_facing:
                new_east_facing.add((nr, nc))
                can_move = True
            else:
                new_east_facing.add((r, c))

        for r, c in south_facing:
            nr, nc = next_south_cell(r, c, m, n)
            if (nr, nc) not in new_east_facing and (nr, nc) not in south_facing:
                new_south_facing.add((nr, nc))
                can_move = True
            else:
                new_south_facing.add((r, c))

        print("Step", step)

        east_facing = new_east_facing
        south_facing = new_south_facing
        region = [["."] * n for _ in range(m)]

        for r, row in enumerate(region):
            for c, cell in enumerate(row):
                if (r, c) in east_facing:
                    region[r][c] = ">"
                elif (r, c) in south_facing:
                    region[r][c] = "v"
            print("".join(row))
        print()

        if not can_move:
            break

    print("Stop after", step)
    return step


if __name__ == "__main__":
    region = read_input("input.txt")
    part_1(region)
