SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
XMAS = "XMAS"

def read_input(file):
    with open(file, "r") as f:
        grid = [line.strip() for line in f.readlines()]
    return grid


def part_1(file):
    grid = read_input(file)
    m, n = len(grid), len(grid[0])

    def count_xmas(start_row, start_col):
        if grid[start_row][start_col] != XMAS[0]:
            return 0
        count = 0
        for dr, dc in DIRS:
            step = 1
            while step < 4:
                ch = XMAS[step]
                nr = start_row + step * dr
                nc = start_col + step * dc
                if nr < 0 or nr >= m:
                    break
                if nc < 0 or nc >= n:
                    break
                if grid[nr][nc] != ch:
                    break
                step += 1
            if step == 4:
                count += 1
        return count


    answer = 0
    for r in range(m):
        for c in range(n):
            answer += count_xmas(r, c)

    print(f"ANSWER: {answer}")

def part_2(file):
    grid = read_input(file)
    m, n = len(grid), len(grid[0])

    def count_xmas(center_row, center_col):
        if grid[center_row][center_col] != 'A':
            return 0
        if center_row == 0 or center_row == m - 1:
            return 0
        if center_col == 0 or center_col == n - 1:
            return 0
        main_diag = "".join([grid[center_row - 1][center_col - 1], grid[center_row + 1][center_col + 1]])
        second_diag = "".join([grid[center_row - 1][center_col + 1], grid[center_row + 1][center_col - 1]])

        if (main_diag == "MS" or main_diag == "SM") and (second_diag == "MS" or second_diag == "SM"):
            return 1
        return 0

    answer = 0
    for r in range(m):
        for c in range(n):
            answer += count_xmas(r, c)
    print(f"ANSWER: {answer}")



if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
