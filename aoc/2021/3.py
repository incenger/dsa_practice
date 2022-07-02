from bisect import bisect_left


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


def part_1(numbers):
    col_sum = [0] * len(numbers[0])

    for number in numbers:
        for i, c in enumerate(number):
            if c == "1":
                col_sum[i] += 1

    gamma_rate = ["1" if col > len(numbers) // 2 else "0" for col in col_sum]
    epsilon_rate = [str(1 - int(x)) for x in gamma_rate]

    power = int("".join(gamma_rate), base=2) * int("".join(epsilon_rate), base=2)

    return power


def part_2(numbers):
    """
    Sort the input
    Use binary search to find the first 1 in column
        - Determine whether 1 is the most common or least common bit
        - Update the left and right of the array and move on
        - The last remaining index is the index of the number to find
    """

    oxy_range = (0, len(numbers) - 1)
    co2_range = (0, len(numbers) - 1)

    bits = [[int(number[i]) for number in numbers] for i in range(len(numbers[0]))]

    def selection(numbers, valid_idx, col, oxy=True):

        if len(valid_idx) == 1:
            return valid_idx

        index_0 = []
        index_1 = []

        for idx in valid_idx:
            if numbers[idx][col] == "1":
                index_1.append(idx)
            else:
                index_0.append(idx)
        count_0 = len(index_0)
        half = len(valid_idx) // 2

        if oxy:
            # 1 is the most common bit
            if count_0 <= half:
                return index_1
            # 0 is the most common bit
            else:
                return index_0
        else:
            # 0 is the least common bit
            if count_0 <= half:
                return index_0
            # 1 is the least common bit
            else:
                return index_1

    oxy_idx = [i for i in range(len(numbers))]
    co2_idx = [i for i in range(len(numbers))]

    for i in range(len(numbers[0])):
        oxy_idx = selection(numbers, oxy_idx, i, True)
        co2_idx = selection(numbers, co2_idx, i, False)

    oxy_rating = int("".join(numbers[oxy_idx[0]]), base=2)
    co2_rating = int("".join(numbers[co2_idx[0]]), base=2)

    return oxy_rating * co2_rating


if __name__ == "__main__":
    numbers = read_input("./input.txt")
    print(part_2(numbers))
