"""
Backtracking with memoization
Try all number from 9 to 1 for each input
Hope that the first solution doesn't take so long -> It does take very long
Early terminate
This brute force occupied a few GB memory
"""
from functools import lru_cache
import sys

sys.setrecursionlimit(10 ** 7)


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
        ops = [l.split() for l in lines]
    return ops


def evaluate(var_or_num, values):
    try:
        num = int(var_or_num)
    except Exception:
        return values[var_or_num]
    return num

@lru_cache(None)
def backtrack(op_idx, x, y, z, w):
    global ops
    # z value tends to be very big for wrong trial
    if z >  10 ** 7:
        return False, ""


    if op_idx >= len(ops):
        return z == 0, ""


    values = {"x": x, "y": y, "z": z, "w": w}

    op = ops[op_idx]
    # print(op_idx, op, values)

    if op[0] == "inp":
        # try all digits
        # for d in range(9, 0, -1):
        for d in range(1, 10):
            values[op[1]] = d
            ok, model_number = backtrack(op_idx + 1, **values)
            if ok:
                model_number = str(d) + model_number
                print("OK", op_idx, values, model_number)
                return ok, model_number
        # Cannot find any
        return False, ""

    values = execute_ops(op, values)
    return backtrack(op_idx + 1, **values)


def execute_ops(op, values):
    """
    values: dict of x, y, z, and w
    """

    if op[0] == "add":
        values[op[1]] += evaluate(op[2], values)
    elif op[0] == "mul":
        values[op[1]] *= evaluate(op[2], values)
    elif op[0] == "div":
        values[op[1]] //= evaluate(op[2], values)
    elif op[0] == "mod":
        values[op[1]] %= evaluate(op[2], values)
    elif op[0] == "eql":
        values[op[1]] = 1 if values[op[1]] == evaluate(op[2], values) else 0
    return values


if __name__ == "__main__":
    ops = read_input("input.txt")
    print(backtrack(0, 0, 0, 0, 0)[1])
