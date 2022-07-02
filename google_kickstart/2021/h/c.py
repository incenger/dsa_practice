"""
A better way to do this: Convert the string to linked list and maintain a lookup table to the node to remove
"""
import re

mapping = "012345678901"
map_rule = [(mapping[i : i + 2], mapping[i+2]) for i in range(len(mapping) - 2)]


def solve(s):
    # O(N^2) -> It needs to build up new string
    # We can do it inplace?
    while True:
        original_s = s
        for x, y in map_rule:
            s = s.replace(x, y)
        if original_s == s:
            break
            if original_s == s:
                break
    return s


if __name__ == "__main__":
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        s = input()

        ans = solve(s)
        print(f"Case #{t}: {ans}")
