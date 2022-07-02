from collections import Counter

"""
Count the number of pairs

"""


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    template = lines[0]
    rules = []
    for line in lines:
        if "->" in line:
            rules.append(tuple(e.strip() for e in line.split("->")))

    return template, rules


def part_1(template, rules, steps):

    for _ in range(steps):
        insert_char = []
        for match, replace in rules:
            for i in range(len(template) - 1):
                if template[i : i + 2] == match:
                    insert_char.append((i + 1, replace))

        insert_char.sort()

        template = list(template)

        for i, (pos, c) in enumerate(insert_char):
            template.insert(pos + i, c)

        template = "".join(template)

        counter = Counter(template)
        print(counter.most_common())
    most_common = counter.most_common()[0][1]
    least_common = counter.most_common()[-1][1]

    return most_common - least_common


def part_2(template, rules, steps):

    pair_counter = Counter()

    for i in range(len(template) - 1):
        pair_counter[template[i : i + 2]] += 1

    rule_map = {match: replace for match, replace in rules}

    for _ in range(steps):
        new_pair_counter = Counter()

        for pair in pair_counter:
            if pair in rule_map:
                new_pair_counter[pair[0] + rule_map[pair]] += pair_counter[pair]
                new_pair_counter[rule_map[pair] + pair[1]] += pair_counter[pair]
            else:
                new_pair_counter[pair] = pair_counter[pair]
        pair_counter = new_pair_counter
        # print(pair_counter)

    char_counter = Counter()

    for pair, count in pair_counter.items():
        for c in pair:
            char_counter[c] += count

    char_counter[template[0]] += 1
    char_counter[template[-1]] += 1

    most_common = char_counter.most_common()[0][1] / 2
    least_common = char_counter.most_common()[-1][1] / 2

    return most_common - least_common


if __name__ == "__main__":
    template, rules = read_input("input.txt")
    ans = part_2(template, rules, 40)
    print(ans)
