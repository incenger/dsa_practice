from collections import defaultdict


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()

    lines = [["".join(sorted(s)) for s in l.split()] for l in lines]

    notes = [(l[:10], l[11:]) for l in lines]
    return notes


def part_1(notes):

    count = 0
    for _, output in notes:
        for signal in output:
            if len(signal) in (2, 3, 4, 7):
                count += 1

    return count


SEGMENTS = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def decode(signals, wire_map):
    output = ""
    for signal in signals:
        correct_signal = "".join(sorted((wire_map[c] for c in signal)))
        output += SEGMENTS[correct_signal]
    return int(output)


def decode_note(signals, outputs):
    wire_map = {}
    length_map = defaultdict(list)

    for signal in signals:
        length_map[len(signal)].append(set(signal))

    # 1 and 7 -> a
    wire_a = (length_map[3][0]  -  length_map[2][0]).pop()
    wire_map[wire_a] = "a"

    # intersection of len == 5 /
    wire_a_d_g = set.intersection(*length_map[5])
    wire_d_g = wire_a_d_g.difference({wire_a})
    wire_d = (wire_d_g & length_map[4][0]).pop()
    wire_g = wire_d_g.difference({wire_d}).pop()
    wire_map[wire_d] = "d"
    wire_map[wire_g] = "g"

    wire_b_d = length_map[4][0].difference(length_map[2][0])
    wire_b = wire_b_d.difference({wire_d}).pop()
    wire_map[wire_b] = "b"

    for signal in length_map[5]:
        if wire_b in signal:
            length_5_with_b = signal

    wire_f = length_5_with_b.difference({wire_a, wire_b, wire_d, wire_g}).pop()
    wire_map[wire_f] = "f"

    wire_c = length_map[2][0].difference({wire_f}).pop()
    wire_map[wire_c] = "c"

    wire_e = (
        length_map[7][0]
        .difference({wire_a, wire_b, wire_c, wire_d, wire_f, wire_g})
        .pop()
    )
    wire_map[wire_e] = "e"

    return decode(outputs, wire_map)


def part_2(notes):
    return sum(decode_note(signal, output) for signal, output in notes)


if __name__ == "__main__":
    notes = read_input("./input.txt")
    count = part_2(notes)
    print(count)
