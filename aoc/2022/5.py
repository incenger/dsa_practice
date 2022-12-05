import string


def parse_input(file):
    with open(file, "r") as f:
        lines = [l.strip("\n") for l in f.readlines()]
    num_containers = len(lines[0]) // 4 + 1
    containers = [[] for _ in range(num_containers)]
    commands = []

    # Parse containers
    for line in lines:
        if "[" in line:
            for container_idx, crate_idx in enumerate(range(1, len(line), 4)):
                if line[crate_idx] != " ":
                    assert line[crate_idx] in string.ascii_letters
                    containers[container_idx].append(line[crate_idx])

        elif line and line[0] == "m":
            words = line.split()
            count, source, dest = int(words[1]), int(words[3]), int(words[5])
            commands.append((count, source, dest))

    for container in containers:
        container.reverse()

    return containers, commands


def move_9000(source_container, dest_container, count):
    assert count <= len(source_container)
    for _ in range(count):
        dest_container.append(source_container.pop())


def move_9001(source_container, dest_container, count):
    assert count <= len(source_container)
    dest_container.extend(source_container[-count:])

    for _ in range(count):
        source_container.pop()


def part_1():
    containers, commands = parse_input("input.txt")

    for count, source, dest in commands:
        source -= 1
        dest -= 1
        move_9000(containers[source], containers[dest], count)

    print("".join(container[-1] for container in containers))


def part_2():
    containers, commands = parse_input("input.txt")

    for count, source, dest in commands:
        source -= 1
        dest -= 1
        move_9001(containers[source], containers[dest], count)

    print("".join(container[-1] for container in containers))


if __name__ == "__main__":
    part_1()
    part_2()
