import string

lower = [c for c in string.ascii_lowercase]


def solve(s, f):
    f = set([c for c in f])
    ans = 0

    for c in s:
        i = lower.index(c)

        k = 0
        while True:
            inc = (i + k) % 26
            dec = ((i - k) + 26) % 26
            if lower[inc] in f or lower[dec] in f:
                op = k
                break
            k += 1
        ans += op

    return ans


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        s = input().strip()
        f = input().strip()
        ans = solve(s, f)
        print(f"Case #{t}: {ans}")
