class Line:
    def __init__(self, x1, y1, x2, y2):
        """
        Store parametric equation of line
        x = at + b
        y = ct + d
        """
        if x1 == x2:
            # Vertical line
            self.type = "V"
            self.x = (0, x1)  # x = x1
            self.y = (1, 0)  # y = t
            self.t = (min(y1, y2), max(y1, y2))
        elif y1 == y2:
            # Horizontal line
            self.type = "H"
            self.x = (1, 0)  # x = t
            self.y = (0, y1)  # y = y1
            self.t = (min(x1, x2), max(x1, x2))
        else:
            # Diagonal line
            self.type = "D"
            if (y2 - y1) * (x2 - x1) > 0:
                self.x = (1, 0)
                self.y = (1, y1 - x1)
                self.t = (min(x1, x2), max(x1, x2))
            else:
                self.x = (1, 0)
                self.y = (-1, y1 + x1)
                self.t = (min(x1, x2), max(x1, x2))

    def __repr__(self):
        return f"({self.type}; {self.x}; {self.y}; {self.t}"

    def intersect(self, other):
        valid_t = (0, -1)  # dummy value

        if self.x[0] == other.x[0]:
            if self.x[0] == 0:
                # Two vertical lines
                # Check the x coordinate and take the common range of t
                if self.x[1] == other.x[1]:
                    valid_t = (max(self.t[0], other.t[0]), min(self.t[1], other.t[1]))
            else:
                # Horizontal or Diagonal lines
                # Solve the equation: at + b =  ct + d
                # If a == c, then b == d
                if self.y[0] == other.y[0]:
                    if self.y[1] == other.y[1]:
                        valid_t = (
                            max(self.t[0], other.t[0]),
                            min(self.t[1], other.t[1]),
                        )
                else:
                    # t = (d - b)/(a - c)
                    numerator = other.y[1] - self.y[1]
                    denominator = other.y[0] - self.y[0]

                    if numerator % denominator == 0:
                        t_intersect = -numerator // denominator
                        if (
                            self.t[0] <= t_intersect <= self.t[1]
                            and other.t[0] <= t_intersect <= other.t[1]
                        ):
                            valid_t = (t_intersect, t_intersect)
        else:
            # One of the two is vertical line
            if self.x[0] == 0:
                return other.intersect(self)
            else:
                # self is not the vertical line
                if self.t[0] <= other.x[1] <= self.t[1]:
                    y_intersect = other.x[1] * self.y[0] + self.y[1]
                    if other.t[0] <= y_intersect <= other.t[1]:
                        valid_t = (other.x[1], other.x[1])

        points = [
            (self.x[0] * t + self.x[1], self.y[0] * t + self.y[1])
            for t in range(valid_t[0], valid_t[1] + 1)
        ]
        return points


def read_input_part_1(file):
    with open(file, "r") as f:
        inputs = f.readlines()

    lines = []
    for inp in inputs:
        xy = inp.split()
        x1, y1 = list(map(int, xy[0].split(",")))
        x2, y2 = list(map(int, xy[2].split(",")))
        line = Line(x1, y1, x2, y2)
        lines.append(line)

    return lines


def part_1(lines):
    interections = set()
    for i, line in enumerate(lines):
        for other_line in lines[i + 1 :]:
            interections.update(line.intersect(other_line))

    return interections


if __name__ == "__main__":
    lines = read_input_part_1("./input.txt")
    points = part_1(lines)
    print(len(points))
