"""
It seems to be a math problem


x1 = x0 + vx
y1 = y0 + vy
vx = vx - 1 if vx > 0
vy = vy - 1

Y equation
Find the maximum value of y
Y = vy0 t - 1/2t^2 (a = -1)
X = vx0 t - 1/2t^2

119, 176
-141 -84


Just simulate
"""

TARGET_X = (119, 176)
TARGET_Y = (-141, -84)

# TARGET_X = (20, 30)
# TARGET_Y = (-10, -5)


def part_1():

    # Just brute force
    # Min vx such that vx(vx+1)/2 >= 119

    ans = float("-inf")

    for vx0 in range(15, 177):
        for vy0 in range(1, 142):
            max_height = vy0 * (vy0 + 1) / 2
            x, y, vx, vy = 0, 0, vx0, vy0
            # It's possible to compute the number of step
            for step in range(1000):
                x += vx
                y += vy
                vx = max(0, vx - 1)
                vy -= 1
                if TARGET_X[0] <= x <= TARGET_X[1] and TARGET_Y[0] <= y <= TARGET_Y[1]:
                    ans = max(ans, max_height)
                    break

    return ans


def part_2():

    ans = set()

    for vx0 in range(1, 200):
        for vy0 in range(-200, 200):
            x, y, vx, vy = 0, 0, vx0, vy0
            for step in range(1000):
                x += vx
                y += vy
                vx = max(0, vx - 1)
                vy -= 1
                if TARGET_X[0] <= x <= TARGET_X[1] and TARGET_Y[0] <= y <= TARGET_Y[1]:
                    ans.add((vx0, vy0))
                    break

    return ans


if __name__ == "__main__":
    print(len(part_2()))
