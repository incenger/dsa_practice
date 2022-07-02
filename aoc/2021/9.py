DIR_R = [0, 1, 0, -1]
DIR_C = [1, 0, -1, 0]


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    heatmap = [[int(c) for c in line.strip()] for line in lines]
    return heatmap


def part_1(heatmap):
    h = len(heatmap)
    w = len(heatmap[0])

    low_point_risk = []
    for r in range(h):
        for c in range(w):
            height = heatmap[r][c]
            is_low_point = True
            for dr, dc in zip(DIR_R, DIR_C):
                adj_r = r + dr
                adj_c = c + dc

                if (
                    0 <= adj_r < h
                    and 0 <= adj_c < w
                    and height >= heatmap[adj_r][adj_c]
                ):
                    is_low_point = False
                    break
            if is_low_point:
                low_point_risk.append(1 + height)
    return sum(low_point_risk)


def part_2(heatmap):
    h = len(heatmap)
    w = len(heatmap[0])

    visited = [[False] * w for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if heatmap[r][c] == 9:
                visited[r][c] = True

    basins = []

    def dfs(r, c):
        visited[r][c] = True
        count = 1
        for dr, dc in zip(DIR_R, DIR_C):
            adj_r = r + dr
            adj_c = c + dc

            if (
                0 <= adj_r < h
                and 0 <= adj_c < w
                and not visited[adj_r][adj_c]
                and height < heatmap[adj_r][adj_c]
            ):
                count += dfs(adj_r, adj_c)
        return count

    for r in range(h):
        for c in range(w):
            if visited[r][c]:
                continue
            height = heatmap[r][c]
            is_low_point = True
            for dr, dc in zip(DIR_R, DIR_C):
                adj_r = r + dr
                adj_c = c + dc

                if (
                    0 <= adj_r < h
                    and 0 <= adj_c < w
                    and height >= heatmap[adj_r][adj_c]
                ):
                    is_low_point = False
                    break
            if is_low_point:
                basins.append(dfs(r, c))

    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


if __name__ == "__main__":
    heatmap = read_input("./input.txt")
    print(part_2(heatmap))
