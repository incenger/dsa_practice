from functools import lru_cache


def create_graph_from_input(input_file):
    valve_name2idx = {}
    valve_idx2name = {}

    with open(input_file, "r") as f:
        lines = [line.strip().split() for line in f.readlines()]

    for line in lines:
        valve_name = line[1]
        if valve_name not in valve_name2idx:
            valve_name2idx[valve_name] = len(valve_name2idx)
            valve_idx2name[valve_name2idx[valve_name]] = valve_name

    n = len(valve_idx2name)
    valve_rate = [0] * n
    graph = [[] for _ in range(n)]

    for line in lines:
        name = line[1]
        idx = valve_name2idx[name]
        rate = int(line[4].split("=")[1][:-1])
        valve_rate[idx] = rate
        neighbors = line[9:]

        for neighbor in neighbors:
            neighbor = neighbor.replace(",", "")
            graph[idx].append(valve_name2idx[neighbor])

    return valve_name2idx, valve_idx2name, valve_rate, graph


def part_1():
    """Ideas: Brute-force with memoization. Use integer or bitset to keep track of opened valve."""

    valve_name2idx, valve_idx2name, valve_rate, graph = create_graph_from_input(
        "input.txt"
    )
    n = len(graph)

    def open_valve(mask, idx):
        return mask | (1 << idx)

    def is_open(mask, idx):
        return (mask & (1 << idx)) > 0

    def floyd_warshall():
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for i in range(n):
            for j in graph[i]:
                dist[i][j] = dist[j][i] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

        return dist

    dist = floyd_warshall()

    START = valve_name2idx["AA"]

    @lru_cache(maxsize=None)
    def brute_force(u, opened_mask, gtime):

        if gtime <= 0:
            return 0

        if valve_rate[u] > 0:
            # Exception: The first valve has 0 rate
            gtime -= 1  # Time for open valve
            pressure = gtime * valve_rate[u]
        else:
            pressure = 0

        new_opened_mask = open_valve(opened_mask, u)
        max_pressure = pressure
        for v in range(n):
            if is_open(new_opened_mask, v) or dist[u][v] > gtime or valve_rate[v] == 0:
                continue

            max_pressure = max(
                max_pressure,
                pressure + brute_force(v, new_opened_mask, gtime - dist[u][v]),
            )

        return max_pressure

    # Mark all valve with rate 0 opended to reduce the memory usage
    # and possibly running time complexity

    initial_mask = 0
    print("Part 1", brute_force(START, initial_mask, 30))


def part_2():
    """Using two timers to for user and elephant, then do similar to the part 1.

    This solution takes a while to run. It could be like 100 times slower than part 1.
    Took 40 minutes ....
    """

    valve_name2idx, valve_idx2name, valve_rate, graph = create_graph_from_input(
        "input.txt"
    )
    n = len(graph)

    def open_valve(mask, idx):
        return mask | (1 << idx)

    def is_open(mask, idx):
        return (mask & (1 << idx)) > 0

    def floyd_warshall():
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for i in range(n):
            for j in graph[i]:
                dist[i][j] = dist[j][i] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

        return dist

    dist = floyd_warshall()

    START = valve_name2idx["AA"]

    @lru_cache(maxsize=None)
    def brute_force(u, e, opened_mask, utime, etime):

        if utime <= 0 and etime <= 0:
            return 0

        # User opens the valve
        new_opened_mask = opened_mask
        if valve_rate[u] > 0 and utime > 0:
            # Exception: The first valve has 0 rate
            utime -= 1  # Time for open valve
            u_pressure = utime * valve_rate[u]
            new_opened_mask = open_valve(new_opened_mask, u)
        else:
            u_pressure = 0

        # Elephant opens the valve
        if valve_rate[e] > 0 and etime > 0 and not is_open(new_opened_mask, e):
            # Exception: The first valve has 0 rate
            etime -= 1  # Time for open valve
            e_pressure = etime * valve_rate[e]
            new_opened_mask = open_valve(new_opened_mask, e)
        else:
            e_pressure = 0

        pressure = u_pressure + e_pressure
        max_pressure = pressure

        # Both either user and elephant has the chance to pick a vertex
        # Hence, there are two loops

        for u_v in range(n):

            if is_open(new_opened_mask, u_v) or valve_rate[u_v] == 0:
                continue

            for e_v in range(n):

                if (
                    u_v
                    == e_v  # User and elephent never opens the same valve, except the first one.
                    or is_open(new_opened_mask, e_v)
                    or valve_rate[e_v] == 0
                ):
                    continue

                max_pressure = max(
                    max_pressure,
                    pressure
                    + brute_force(
                        u_v,
                        e_v,
                        new_opened_mask,
                        max(utime - dist[u][u_v], 0),
                        max(etime - dist[e][e_v], 0),
                    ),
                )

                max_pressure = max(
                    max_pressure,
                    pressure
                    + brute_force(
                        e_v,
                        u_v,
                        new_opened_mask,
                        max(utime - dist[u][e_v], 0),
                        max(etime - dist[e][u_v], 0),
                    ),
                )

        return max_pressure

    # Mark all valve with rate 0 opended to reduce the memory usage
    # and possibly running time complexity

    initial_mask = 0
    print("Part 2", brute_force(START, START, initial_mask, 26, 26))


if __name__ == "__main__":
    part_1()
    part_2()
