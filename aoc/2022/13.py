from functools import cmp_to_key


def is_right_order(packet_1, packet_2):
    if isinstance(packet_1, int) and isinstance(packet_2, int):
        if packet_1 > packet_2:
            return 1
        elif packet_1 < packet_2:
            return -1
        else:
            return 0

    if not isinstance(packet_1, list):
        packet_1 = [packet_1]

    if not isinstance(packet_2, list):
        packet_2 = [packet_2]

    i, j = 0, 0
    while i < len(packet_1) and j < len(packet_2):
        right_order = is_right_order(packet_1[i], packet_2[j])
        if right_order != 0:
            return right_order
        i += 1
        j += 1

    if i == len(packet_1) and j == len(packet_2):
        return 0
    elif i < len(packet_1):
        return 1
    else:
        return -1


def part_1_2():
    with open("input.txt", "r") as f:
        packets = [eval(line.strip()) for line in f.readlines() if line != "\n"]

    sum_correct_packect_pair_idx = 0

    for i in range(0, len(packets), 2):
        first_packet = packets[i]
        second_packet = packets[i + 1]

        if is_right_order(first_packet, second_packet) == -1:
            sum_correct_packect_pair_idx += i // 2 + 1

    print("Part 1", sum_correct_packect_pair_idx)

    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(is_right_order))
    decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

    print("Part 2", decoder_key)


if __name__ == "__main__":
    part_1_2()
