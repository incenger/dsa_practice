def priority(ch):
    ord_ch = ord(ch)

    return 1 + ord_ch - ord('a') if ord_ch >= ord('a') else 27 + ord_ch - ord('A')

def part_1():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    res = 0
    for line in lines:
        l = len(line)
        first_compartment = line[:l//2]
        second_compartment = line[l//2:]
        res += sum(priority(ch) for ch in set(first_compartment) & set(second_compartment))

    print(res)

def part_2():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    res = 0
    for i in range(0, len(lines), 3):
        groups = lines[i:i+3]
        badge = set.intersection(*map(set, groups)).pop()
        res += priority(badge)

    print(res)


if __name__ == "__main__":
    part_1()
    part_2()
