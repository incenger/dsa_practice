class Board:
    def __init__(self, lines):
        self.board = []
        self.marked = [[False] * 5 for _ in range(5)]
        for line in lines:
            self.board.append(list(map(int, line.split())))
        self.value_location = {
            v: (i, j) for i, row in enumerate(self.board) for j, v in enumerate(row)
        }
        self.column_mark = [0] * 5
        self.row_mark = [0] * 5
        self.bingo = False

    def mark(self, value):
        if value not in self.value_location:
            return

        row, col = self.value_location[value]
        self.marked[row][col] = True
        self.column_mark[col] += 1
        self.row_mark[row] += 1

    def bingo_score(self):
        return sum(
            [
                v
                for i, row in enumerate(self.board)
                for j, v in enumerate(row)
                if not self.marked[i][j]
            ]
        )

    def is_bingo(self):
        if self.bingo:
            return True

        self.bingo = any([x == 5 for x in self.column_mark]) or any(
            [x == 5 for x in self.row_mark]
        )
        return self.bingo

    def _mark(self, row, col):
        self.marked[row][col] = True


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if l]

    draw_numbers = list(map(int, lines[0].split(",")))
    boards = []

    for i in range(1, len(lines) - 4, 5):
        boards.append(Board(lines[i : i + 5]))

    return draw_numbers, boards


def part_1_2(draw_numbers, boards, first=True):

    last = None

    for number in draw_numbers:

        for board in boards:
            if board.is_bingo():
                continue
            else:
                board.mark(number)
                if board.is_bingo():
                    if first:
                        return number * board.bingo_score()
                    last = number * board.bingo_score()
    return last


if __name__ == "__main__":
    ans = part_1_2(*read_input("./input.txt"), False)
    print(ans)
