"""
time python3 8.py
python3 8.py  0.02s user 0.02s system 77% cpu 0.049 total
"""

import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    city_map = []
    with open(file, "r") as f:
        for line in f.readlines():
            city_map.append(list(line.strip()))
    return city_map


def part_1(file):
    city_map = read_input(file)
    m, n = len(city_map), len(city_map[0])
    antenna_by_signal = collections.defaultdict(list)

    for r in range(m):
        for c in range(n):
            if city_map[r][c] != '.':
                antenna_by_signal[city_map[r][c]].append((r, c))

    def check_map_boundary(location):
        return 0 <= location[0] < m and 0 <= location[1] < n

    antinodes = set()
    for cities in antenna_by_signal.values():
        for i in range(len(cities)):
            row_a, col_a = cities[i]
            for j in range(i + 1, len(cities)):
                row_b, col_b = cities[j]
                d_row, d_col = row_b - row_a, col_b - col_a
                first_antinode = (row_a - d_row, col_a - d_col)
                if check_map_boundary(first_antinode):
                    antinodes.add(first_antinode)
                second_antinode = (row_a + 2 * d_row, col_a + 2 * d_col)
                if check_map_boundary(second_antinode):
                    antinodes.add(second_antinode)

    answer = len(antinodes)
    print("ANSWER:", answer)


def part_2(file):
    city_map = read_input(file)
    m, n = len(city_map), len(city_map[0])
    antenna_by_signal = collections.defaultdict(list)

    for r in range(m):
        for c in range(n):
            if city_map[r][c] != '.':
                antenna_by_signal[city_map[r][c]].append((r, c))

    def check_map_boundary(location):
        return 0 <= location[0] < m and 0 <= location[1] < n

    antinodes = set()
    for cities in antenna_by_signal.values():
        for i in range(len(cities)):
            row_a, col_a = cities[i]
            for j in range(i + 1, len(cities)):
                row_b, col_b = cities[j]
                d_row, d_col = row_b - row_a, col_b - col_a
                # Forward and backward step until we're out of the map
                step = 0
                while True:
                    forward_antinode = (row_a + step * d_row,
                                        col_a + step * d_col)
                    backward_antinode = (row_a - step * d_row,
                                         col_a - step * d_col)

                    if check_map_boundary(forward_antinode):
                        antinodes.add(forward_antinode)

                    if check_map_boundary(backward_antinode):
                        antinodes.add(backward_antinode)

                    if not (check_map_boundary(forward_antinode)
                            or check_map_boundary(backward_antinode)):
                        break
                    step += 1

    answer = len(antinodes)
    print("ANSWER:", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
