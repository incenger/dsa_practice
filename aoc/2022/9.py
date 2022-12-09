def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def compute_tail_displacement(dis_vector):
    # Given the displacement vector from T to H
    # Compute the displacement vector to the next position the tail should head to
    dx, dy = dis_vector
    if abs(dx) < 2 and abs(dy) < 2:
        # The head is in close proximity of the tail
        # No movement needed
        return (0, 0)
    return (sign(dx), sign(dy))


HEAD_DISPLACEMENT_PARSER = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def part_1():
    with open("input.txt", "r") as f:
        head_moves = [line.split() for line in f.readlines()]

    head_pos = (0, 0)
    tail_pos = (0, 0)
    tail_visited = set()
    tail_visited.add(tail_pos)

    for head_move in head_moves:
        direction, step = head_move
        for _ in range(int(step)):
            head_dis = HEAD_DISPLACEMENT_PARSER[direction]
            head_pos = (head_pos[0] + head_dis[0], head_pos[1] + head_dis[1])
            tail_to_head = (head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1])
            tail_dis = compute_tail_displacement(tail_to_head)
            tail_pos = (tail_pos[0] + tail_dis[0], tail_pos[1] + tail_dis[1])

            tail_visited.add(tail_pos)
    print("Part 1", len(tail_visited))


def part_2():
    with open("input.txt", "r") as f:
        head_moves = [line.split() for line in f.readlines()]

    N_KNOTS = 9

    head_pos = (0, 0)
    knots_pos = [(0, 0)] * N_KNOTS
    tail_visited = set()
    tail_visited.add(knots_pos[-1])

    for head_move in head_moves:
        direction, step = head_move
        for _ in range(int(step)):
            head_dis = HEAD_DISPLACEMENT_PARSER[direction]
            head_pos = (head_pos[0] + head_dis[0], head_pos[1] + head_dis[1])

            # Iteratively update knot position
            for i in range(N_KNOTS):
                next_knot = head_pos if i == 0 else knots_pos[i - 1]
                cur_knot = knots_pos[i]
                to_next_knot = (
                    next_knot[0] - cur_knot[0],
                    next_knot[1] - cur_knot[1],
                )
                knot_dis = compute_tail_displacement(to_next_knot)
                knots_pos[i] = (
                    cur_knot[0] + knot_dis[0],
                    cur_knot[1] + knot_dis[1],
                )

            tail_visited.add(knots_pos[-1])

    print("Part 2", len(tail_visited))


if __name__ == "__main__":
    part_1()
    part_2()
