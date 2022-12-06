from collections import defaultdict


def naive(buffer, window_size):

    for i in range(window_size - 1, len(buffer)):
        if len(set(buffer[i - window_size + 1 : i + 1])) == window_size:
            return i + 1

    return None


def sliding_window(buffer, window_size):
    distinct_cnt = 0
    counter = defaultdict(int)

    for i in range(window_size - 1):
        if counter[buffer[i]] == 0:
            distinct_cnt += 1
        counter[buffer[i]] += 1

    for i in range(window_size - 1, len(buffer)):

        if counter[buffer[i]] == 0:
            distinct_cnt += 1
        counter[buffer[i]] += 1

        if distinct_cnt == window_size:
            return i + 1

        counter[buffer[i - window_size + 1]] -= 1
        if counter[buffer[i - window_size + 1]] == 0:
            distinct_cnt -= 1


def part_1_2():
    with open("input.txt") as f:
        buffer = f.readline().strip()
    print(naive(buffer, 4))
    print(naive(buffer, 14))

    print(sliding_window(buffer, 4))
    print(sliding_window(buffer, 14))


if __name__ == "__main__":
    part_1_2()
