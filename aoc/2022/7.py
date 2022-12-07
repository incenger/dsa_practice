import os


class Object:
    def __init__(self, identifier, is_dir=True, size=0, parent=None):
        self.identifier = identifier
        self.size = size
        self.is_dir = is_dir
        self.children = {}
        self.parent = parent


def size_of(obj):
    if obj.is_dir:
        dir_size = 0
        for child in obj.children.values():
            dir_size += size_of(child)
        obj.size = dir_size
    return obj.size


def total_size(obj, limit):
    if not obj.is_dir:
        return 0
    size = 0 if obj.size > limit else obj.size
    for child in obj.children.values():
        if child.is_dir:
            size += total_size(child, limit)
    return size


def find_dirs(obj, found):
    if not obj.is_dir:
        return
    found.append(obj)
    for child in obj.children.values():
        if child.is_dir:
            find_dirs(child, found)


def part_1_2():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    pc = 0
    root = Object("/")
    working_dir = root
    lines.pop(0)
    while pc < len(lines):

        command = lines[pc]

        if "cd" in command:
            dest = command.split()[2]
            if dest == "..":
                working_dir = working_dir.parent
                assert working_dir is not None
            else:
                children_identifier = working_dir.identifier + os.sep + dest
                working_dir = working_dir.children[children_identifier]
            pc += 1
        else:
            ls_output_idx = pc + 1
            while ls_output_idx < len(lines) and lines[ls_output_idx][0] != "$":
                ls_output_idx += 1

            for i in range(pc + 1, ls_output_idx):
                size_or_dir, name = lines[i].split()
                children_identifier = working_dir.identifier + os.sep + name
                if size_or_dir == "dir":
                    working_dir.children.setdefault(
                        children_identifier,
                        Object(children_identifier, parent=working_dir),
                    )
                else:
                    size = int(size_or_dir)
                    working_dir.children.setdefault(
                        children_identifier,
                        Object(
                            children_identifier,
                            is_dir=False,
                            size=size,
                            parent=working_dir,
                        ),
                    )

            pc = ls_output_idx

    size_of(root)
    print("Part 1", total_size(root, 100000))

    current_size = root.size
    TOTAL_DISK_SIZE = 70000000
    UPDATE_REQ_SIZE = 30000000
    min_delete_size = UPDATE_REQ_SIZE - (TOTAL_DISK_SIZE - current_size)
    assert min_delete_size > 0

    all_dirs = []
    find_dirs(root, all_dirs)
    all_dirs.sort(key=lambda obj: obj.size)

    for obj in all_dirs:
        if obj.size >= min_delete_size:
            best_to_delete = obj
            break

    print("Part 2", best_to_delete.size)


if __name__ == "__main__":
    part_1_2()
