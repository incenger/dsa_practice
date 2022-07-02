from functools import reduce
from operator import mul


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()

    packets = [l.strip() for l in lines]
    return packets


def hex2bin(hex_str):

    bin_str = ""
    for hex_c in hex_str:
        bin_c = bin(int(hex_c, 16))[2:].zfill(4)
        bin_str += bin_c

    return bin_str


def bin2dec(bin_str):
    return int(bin_str, 2)


def parse_packet(bin_str, offset=0):
    """
    Parse a packet, return its version, type and subpacket
    """
    packet_version = bin2dec(bin_str[offset : offset + 3])
    packet_type_id = bin2dec(bin_str[offset + 3 : offset + 6])

    if packet_type_id == 4:
        # Literal value packet
        i = offset + 6
        value = ""
        is_last_group = False
        while not is_last_group:
            group = bin_str[i : i + 5]
            is_last_group = group[0] == "0"
            value += group[1:]
            i += 5
        value = bin2dec(value)
        offset_next_packet = i
        packet = {
            "version": packet_version,
            "type_id": packet_type_id,
            "value": value,
            "offset": i,
        }
    else:
        length_type_id = bin2dec(bin_str[offset + 6])

        if length_type_id == 0:
            total_sub_packet_length = bin2dec(bin_str[offset + 7 : offset + 22])

            sub_packets = []
            current_subpacket_offset = offset + 22

            while total_sub_packet_length > 0:
                sub_packet = parse_packet(bin_str, current_subpacket_offset)
                sub_packets.append(sub_packet)
                next_subpacket_offset = sub_packet["offset"]
                total_sub_packet_length -= (
                    next_subpacket_offset - current_subpacket_offset
                )
                current_subpacket_offset = next_subpacket_offset

            packet = {
                "version": packet_version,
                "type_id": packet_type_id,
                "value": sub_packets,
                "offset": current_subpacket_offset,
            }
        else:
            total_sub_packet = bin2dec(bin_str[offset + 7 : offset + 18])

            current_subpacket_offset = offset + 18
            sub_packets = []

            for _ in range(total_sub_packet):
                sub_packet = parse_packet(bin_str, current_subpacket_offset)
                sub_packets.append(sub_packet)
                current_subpacket_offset = sub_packet["offset"]

            packet = {
                "version": packet_version,
                "type_id": packet_type_id,
                "value": sub_packets,
                "offset": current_subpacket_offset,
            }

    return packet


def part_1(packet_hex):
    packet = parse_packet(hex2bin(packet_hex))

    def sum_version(packet):
        if packet["type_id"] == 4:
            return packet["version"]
        else:
            return packet["version"] + sum(
                sum_version(sub_packet) for sub_packet in packet["value"]
            )

    return sum_version(packet)


def compute_packet(packet):
    if packet["type_id"] == 4:
        return packet["value"]
    elif packet["type_id"] == 0:
        return sum(compute_packet(sub_packet) for sub_packet in packet["value"])
    elif packet["type_id"] == 1:
        return reduce(
            mul, [compute_packet(sub_packet) for sub_packet in packet["value"]]
        )
    elif packet["type_id"] == 2:
        return min(compute_packet(sub_packet) for sub_packet in packet["value"])
    elif packet["type_id"] == 3:
        return max(compute_packet(sub_packet) for sub_packet in packet["value"])
    elif packet["type_id"] == 5:
        return (
            1
            if compute_packet(packet["value"][0]) > compute_packet(packet["value"][1])
            else 0
        )
    elif packet["type_id"] == 6:
        return (
            1
            if compute_packet(packet["value"][0]) < compute_packet(packet["value"][1])
            else 0
        )
    elif packet["type_id"] == 7:
        return (
            1
            if compute_packet(packet["value"][0]) == compute_packet(packet["value"][1])
            else 0
        )


def part_2(packet_hex):
    packet = parse_packet(hex2bin(packet_hex))
    return compute_packet(packet)


if __name__ == "__main__":
    packets = read_input("example.txt")
    for packet in packets:
        print(part_2(packet))
