def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return list(map(int, lines[0].split(",")))


def part_1(positions):
    """ """
    positions.sort()

    crabs = len(positions)

    # Cost at 0, all positions >=0
    cost = sum(positions)
    min_cost = cost

    for i, pos in enumerate(positions):
        diff = pos if i == 0 else pos - positions[i - 1]
        cost = cost + diff * (2 * i - crabs)
        min_cost = min(cost, min_cost)
        # print(diff, pos, cost)

    return min_cost


def part_2(positions):
    """
    Moving n steps require: n(n+1)/2

    Mathematically, the optimal arrangement value is between mean(x) +1/2 and mean(x) - 1/2


    """
    mean = int(sum(positions) / len(positions))

    return min(
        sum(((x - p) ** 2 + abs(x - p)) / 2 for x in positions)
        for p in range(mean - 1, mean + 2)
    )


if __name__ == "__main__":
    positions = read_input("./input.txt")
    print(part_2(positions))
