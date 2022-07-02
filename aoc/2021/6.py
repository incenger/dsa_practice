import numpy as np
from functools import lru_cache

@lru_cache(None)
def part_2_recursion(population, day, remain):
    if day == 0:
        return population

    if remain == 0:
        current = part_2_recursion(population, day - 1, 6)
        newborn = part_2_recursion(population, day - 1, 8)
        return current + newborn

    return part_2_recursion(population, day - 1, remain - 1)

def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    ages = list(map(int, lines[0].split(",")))
    return ages




def part_2(ages, max_day):
    # All timer
    counts = [0] * 9
    for age in ages:
        counts[age] += 1

    for _ in range(max_day):
        newborn = counts[0]
        for i in range(8):
            counts[i] = counts[i + 1]
        counts[6] += newborn
        counts[8] = newborn

    return sum(counts)


def part_1(ages, day=80):
    # SLOW and Memory Intensive
    while day:
        day -= 1
        newborn = np.count_nonzero(ages == 0)
        ages -= 1
        # Replace the timer
        ages = np.where(ages == -1, 6, ages)
        # Add newborn
        ages = np.concatenate([ages, np.array([8] * newborn)])
        print(ages)
    return ages


if __name__ == "__main__":
    ages = read_input("./input.txt")
    total = sum(part_2_recursion(1, 256, age) for age in ages)
    print(total)
