"""
YGB -> YB -> 2 strokes 1 2 1
YBG -> YBBY -> YBY 3 strokes 1 1 2 
BGB -> 2 strokes 1 2 1
YGY -> 2 strokes 1 2 1
YBY -> 3 strokes  1 1 1
YGBG -> 4 strokes
YY
 BBB
   Y
YYBY
YBBY
"""

COLOR_MAP = {
    "R": ["R", "O", "A", "P"],
    "Y": ["Y", "O", "G", "A"],
    "B": ["B", "P", "G", "A"],
}


def solve(p, color):
    n = len(p)
    stroke = 0
    painting = False

    for i in range(n):
        if p[i] in COLOR_MAP[color]:
            if not painting:
                stroke += 1
                painting = True
        else:
            painting = False
    return stroke


if __name__ == "__main__":
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        p = list(input())

        ans = 0
        for c in COLOR_MAP:
            ans += solve(p, c)

        print(f"Case #{t}: {ans}")
