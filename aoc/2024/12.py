"""
time python3 12.py
python3 12.py  0.17s user 0.02s system 96% cpu 0.194 total
"""

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input(file):
    garden = []
    with open(file, "r") as f:
        for line in f.readlines():
            garden.append(list(line.strip()))
    return garden


def part_1(file):
    garden = read_input(file)
    m, n = len(garden), len(garden[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(row, col):
        visited[row][col] = True
        area = 1
        peri = 0

        for dr, dc in DIRS:
            next_row = row + dr
            next_col = col + dc

            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or garden[
                    next_row][next_col] != garden[row][col]:
                peri += 1
            elif not visited[next_row][next_col]:
                next_area, next_peri = dfs(next_row, next_col)
                peri += next_peri
                area += next_area
        return area, peri

    answer = 0
    for row in range(m):
        for col in range(n):
            if not visited[row][col]:
                area, peri = dfs(row, col)
                answer += area * peri
    print("ANSWER", answer)


def part_2(file):
    # Idea: Count the consecutive edges, scaling the map to represent edges
    garden = read_input(file)
    m, n = len(garden), len(garden[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(row, col, region):
        region.add((row, col))
        visited[row][col] = True

        for dr, dc in DIRS:
            next_row = row + dr
            next_col = col + dc

            if 0 <= next_row < m and 0 <= next_col < n and garden[next_row][
                    next_col] == garden[row][col] and (next_row,
                                                       next_col) not in region:
                dfs(next_row, next_col, region)

    # Split each cell to three and get only the boundary
    def get_micro_cells(region, scale=3):
        all_micro_cells = set()
        for row, col in region:

            # Initialize all borders
            micro_cells = set()
            for i in [0, scale - 1]:
                for j in range(scale):
                    micro_cells.add((scale * row + i, scale * col + j))
            for j in [0, scale - 1]:
                for i in range(scale):
                    micro_cells.add((scale * row + i, scale * col + j))

            # Remove adjacent edge
            if (row - 1, col) in region:
                for i in range(1, scale - 1):
                    micro_cells.remove((scale * row, scale * col + i))

            if (row + 1, col) in region:
                for i in range(1, scale - 1):
                    micro_cells.remove(
                        (scale * row + scale - 1, scale * col + i))

            if (row, col - 1) in region:
                for i in range(1, scale - 1):
                    micro_cells.remove((scale * row + i, scale * col))

            if (row, col + 1) in region:
                for i in range(1, scale - 1):
                    micro_cells.remove(
                        (scale * row + i, scale * col + scale - 1))

            # Remove adjacent corner
            # Top left
            if (row - 1, col - 1) in region and (row - 1, col) in region and (
                    row, col - 1) in region:
                micro_cells.remove((scale * row, scale * col))

            # Top right
            if (row - 1, col + 1) in region and (row - 1, col) in region and (
                    row, col + 1) in region:
                micro_cells.remove((scale * row, scale * col + scale - 1))

            # Bottom left
            if (row + 1, col - 1) in region and (row + 1, col) in region and (
                    row, col - 1) in region:
                micro_cells.remove((scale * row + scale - 1, scale * col))

            # Bottom right
            if (row + 1, col + 1) in region and (row + 1, col) in region and (
                    row, col + 1) in region:
                micro_cells.remove(
                    (scale * row + scale - 1, scale * col + scale - 1))

            all_micro_cells.update(micro_cells)
        return all_micro_cells

    def count_edges(micro_map, region_measurement):
        n_rows, n_cols = len(micro_map), len(micro_map[0])

        for i in range(n_rows):
            edge_length = 0
            prev = -1
            for j in range(n_cols):
                if micro_map[i][j] == -1:
                    edge_length = 0
                elif micro_map[i][j] == prev:
                    edge_length += 1
                else:
                    edge_length = 1
                prev = micro_map[i][j]
                if edge_length == 2:
                    region_measurement[micro_map[i][j]][1] += 1

        for j in range(n_cols):
            edge_length = 0
            prev = -1
            for i in range(n_rows):
                if micro_map[i][j] == -1:
                    edge_length = 0
                elif micro_map[i][j] == prev:
                    edge_length += 1
                else:
                    edge_length = 1
                prev = micro_map[i][j]
                if edge_length == 2:
                    region_measurement[micro_map[i][j]][1] += 1

    SCALE = 3
    answer = 0
    region_id = 0
    micro_map = [[-1] * (SCALE * n) for _ in range(SCALE * m)]
    region_measurement = {}
    for row in range(m):
        for col in range(n):
            if visited[row][col]:
                continue
            region = set()
            dfs(row, col, region)
            micro_cells = get_micro_cells(region, SCALE)
            for x, y in micro_cells:
                micro_map[x][y] = region_id
            region_measurement[region_id] = [len(region), 0]
            region_id += 1

    count_edges(micro_map, region_measurement)
    answer = 0
    for area, edges in region_measurement.values():
        answer += area * edges
    print("ANSWER", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
