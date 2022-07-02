"""
parse_exp: Read the input string and create list or pairs?
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]

[[[0,[4,5]],[0,0]],[[[[5,6],5],[2,6]],[9,5]]]

Need to store the numbers an depths

numbers: 0 4 5 0 0 4 5 2 6 9 5
depth: 3 4 2 3 1 4 3 4 2 2
depth of the pair
how to get the value of the pair given the depth

Pair index -> number index: i -> (i, i+1)

add: add string + (left_depth + 1, 1, right_depth + 1)
explode: find first index of depth 5 -> idx
    - numbers[idx - 1] += numbers[idx]
    - numbers[idx + 2] += numbers[idx + 1]
    - new_numbers = numbers[:idx] +  [0] + numbers[idx+2:]
    - depths = depths[:idx] + depths[idx+1:] #Remove pair at index does not affect the detp of other

split
    - numbers = numbers[:idx]  + new pair + numbers[idx+1:]
    - depths:  max of two surrouding depths, split_idx -> split_idx, split_idx  - 1

magintude:
    - add numbers to a stack
    - If the depth falls, pop from the stack and calculate
"""

import math
from functools import reduce


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    return lines


def parse_snailfish(snailfish):
    numbers = []
    depths = []
    current_depth = 0

    for c in snailfish:
        if c == "[":
            current_depth += 1
        elif c == "]":
            current_depth -= 1
        elif c == ",":
            depths.append(current_depth)
        else:
            numbers.append(int(c))

    return numbers, depths


def add_snailfish(left_sf, right_sf):
    left_numbers, left_depths = left_sf
    right_numbers, right_depths = right_sf

    added_numbers = left_numbers + right_numbers
    added_depths = [1 + d for d in left_depths] + [1] + [1 + d for d in right_depths]
    added_sf = (added_numbers, added_depths)
    return reduce_snailfish(added_sf)


def explode_snailfish(sf):
    numbers, depths = sf
    try:
        explode_idx = depths.index(5)
    except ValueError:
        return sf, False

    if explode_idx > 0:
        numbers[explode_idx - 1] += numbers[explode_idx]
    if explode_idx + 2 < len(numbers):
        numbers[explode_idx + 2] += numbers[explode_idx + 1]
    new_numbers = numbers[:explode_idx] + [0] + numbers[explode_idx + 2 :]
    new_depths = depths[:explode_idx] + depths[explode_idx + 1 :]
    return (new_numbers, new_depths), True


def split_snailfish(sf):
    numbers, depths = sf
    split_idx = -1
    for i, x in enumerate(numbers):
        if x >= 10:
            split_idx = i
            break
    if split_idx == -1:
        return sf, False

    new_pair = [
        math.floor(numbers[split_idx] / 2),
        math.ceil(numbers[split_idx] / 2),
    ]
    new_numbers = numbers[:split_idx] + new_pair + numbers[split_idx + 1 :]
    new_depth = 1 + max(
        depths[split_idx - 1] if split_idx > 0 else 0,
        depths[split_idx] if split_idx < len(depths) else 0,
    )
    new_depths = depths[:split_idx] + [new_depth] + depths[split_idx:]
    return (new_numbers, new_depths), True


def reduce_snailfish(sf):
    while True:
        sf, flag = explode_snailfish(sf)
        if flag:
            continue
        sf, flag = split_snailfish(sf)
        if not flag:
            break
    return sf


def magnitude_snailfish(sf):
    def magnitude(stack):
        stack.append(2 * stack.pop() + 3 * stack.pop())

    stack = []
    numbers, depths = sf
    prev_depth = 0
    for number, depth in zip(numbers, depths):
        stack.append(number)

        for _ in range(prev_depth - depth):
            magnitude(stack)

        prev_depth = depth

    stack.append(numbers[-1])
    while len(stack) > 1:
        magnitude(stack)

    return stack.pop()


def part_1(sfs):
    added_sf = reduce(add_snailfish, sfs)
    reduced_sf = reduce_snailfish(added_sf)
    return magnitude_snailfish(reduced_sf)


def part_2(sfs):
    n = len(sfs)
    max_m = float("-inf")

    for i in range(n):
        for j in range(n):
            if i != j:
                max_m = max(magnitude_snailfish(add_snailfish(sfs[i], sfs[j])), max_m)

    return max_m


if __name__ == "__main__":
    lines = read_input("input.txt")
    sfs = [parse_snailfish(line) for line in lines]
    # for sf in sfs:
    #     print(magnitude_snailfish(reduce_snailfish(sf)))
    m = part_2(sfs)
    print(m)
