"""
time python3 9.py
python3 9.py  0.73s user 0.02s system 98% cpu 0.765 total
"""

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    with open(file, "r") as f:
        return list(map(int, f.readline().strip()))


def compute_checksum(offset, block_size, block_id):
    return (2 * offset + block_size - 1) * block_size * block_id // 2


def part_1(file):
    disk_map = read_input(file)
    file_blocks = []
    space_blocks = []
    for idx, block_size in enumerate(disk_map):
        if idx % 2 == 0:
            # file_block_id = idx // 2
            file_blocks.append([block_size, idx // 2])
        else:
            space_blocks.append(block_size)

    checksum = 0
    file_idx, space_idx = 0, 0
    move_idx = len(file_blocks) - 1
    compact_idx = 0

    while file_idx < len(file_blocks):
        # Fill initial files
        file_size = file_blocks[file_idx][0]
        file_id = file_blocks[file_idx][1]
        checksum += compute_checksum(compact_idx, file_size, file_id)
        compact_idx += file_size
        file_idx += 1

        if file_idx > move_idx:
            break

        # Fill the space
        while space_idx < len(space_blocks) and space_blocks[space_idx]:
            fill_size = min(file_blocks[move_idx][0], space_blocks[space_idx])
            fill_id = file_blocks[move_idx][1]
            checksum += compute_checksum(compact_idx, fill_size, fill_id)
            compact_idx += fill_size

            file_blocks[move_idx][0] -= fill_size
            space_blocks[space_idx] -= fill_size

            if file_blocks[move_idx][0] == 0:
                move_idx -= 1
        space_idx += 1
    print("ANSWER:", checksum)


def part_2(file):
    disk_map = read_input(file)
    file_blocks = []
    space_blocks = []
    for idx, block_size in enumerate(disk_map):
        if idx % 2 == 0:
            # file_block_id = idx // 2
            file_blocks.append([block_size, idx // 2])
        else:
            space_blocks.append(block_size)

    checksum = 0
    moved_files = set()
    space_filled = [[] for _ in range(len(space_blocks))]

    for file_idx in range(len(file_blocks) - 1, -1, -1):
        file_block_size, file_id = file_blocks[file_idx]
        # Find a space to move this block
        for space_idx in range(file_idx):
            space_size = space_blocks[space_idx]
            if space_size >= file_block_size:
                space_blocks[space_idx] -= file_block_size
                space_filled[space_idx].append((file_block_size, file_id))
                moved_files.add(file_id)
                break

    compact_idx = 0
    for idx in range(len(file_blocks)):
        file_id = file_blocks[idx][1]
        block_size = file_blocks[idx][0]
        if file_id not in moved_files:
            checksum += compute_checksum(compact_idx, block_size, file_id)
        compact_idx += block_size

        # Add spaces
        if idx < len(space_filled):
            for moved_block_size, moved_file_id in space_filled[idx]:
                checksum += compute_checksum(compact_idx, moved_block_size,
                                             moved_file_id)
                compact_idx += moved_block_size
            compact_idx += space_blocks[idx]

    print("ANSWER:", checksum)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
