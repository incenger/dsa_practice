def part_1(input_file):
    # O(N^3) solution
    with open(input_file, "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    number_with_idx = list(enumerate(numbers))
    working_copy = number_with_idx[::]
    n = len(number_with_idx)

    for pair in number_with_idx:
        # Find the position in the working copy
        cur_pos = working_copy.index(pair)
        value = pair[1]

        next_pos = (cur_pos + value) % (n - 1)
        if next_pos == 0:
            # A move to the start moves the number to the end of the list
            next_pos = n
        working_copy.insert(next_pos, working_copy.pop(cur_pos))

    idx_of_zero = -1

    for i in range(n):
        if working_copy[i][1] == 0:
            idx_of_zero = i
            break

    assert idx_of_zero != -1
    s = 0
    for offset in (1000, 2000, 3000):
        val = working_copy[(idx_of_zero + offset) % n][1]
        print(val)
        s += val

    print("Part 1", s)


def part_2(input_file):
    # O(N^3) solution
    key = 811589153
    with open(input_file, "r") as f:
        numbers = [int(line.strip()) * key for line in f.readlines()]

    number_with_idx = list(enumerate(numbers))
    working_copy = number_with_idx[::]
    n = len(number_with_idx)

    for _ in range(10):
        for pair in number_with_idx:
            # Find the position in the working copy
            cur_pos = working_copy.index(pair)
            value = pair[1]

            next_pos = (cur_pos + value) % (n - 1)
            if next_pos == 0:
                # A move to the start moves the number to the end of the list
                next_pos = n
            working_copy.insert(next_pos, working_copy.pop(cur_pos))

    idx_of_zero = -1

    for i in range(n):
        if working_copy[i][1] == 0:
            idx_of_zero = i
            break

    assert idx_of_zero != -1
    s = 0
    for offset in (1000, 2000, 3000):
        val = working_copy[(idx_of_zero + offset) % n][1]
        print(val)
        s += val

    print("Part 2", s)


# 4, -2, 5, 6, 7, 8, 9, 4, -2, 5, 6, 7, 8, 9, 4, -2, 5, 6, 7, 8, 9
if __name__ == "__main__":
    part_1("input.txt")
    part_2("input.txt")
