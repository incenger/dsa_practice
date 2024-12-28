"""
time python3 25.py
python3 25.py  0.05s user 0.02s system 89% cpu 0.075 total
"""
SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    semantics = [[]]
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                semantics[-1].append(list(line))
            else:
                semantics.append([])
    return semantics


def height_encoding(semantic):
    encoding = [-1] * len(semantic[0])
    for row in semantic:
        for col_idx, ch in enumerate(row):
            if ch == '#':
                encoding[col_idx] += 1
    is_lock = semantic[0][0] == '#'
    return tuple(encoding), is_lock


def part_1(file):
    semantics = read_input(file)
    height_encodings = list(map(height_encoding, semantics))
    lock_encodings = []
    key_encodings = []
    for semantic in semantics:
        encoding, is_lock = height_encoding(semantic)
        if is_lock:
            lock_encodings.append(encoding)
        else:
            key_encodings.append(encoding)

    answer = 0
    MAX_HEIGHT = 5
    for key_encoding in key_encodings:
        for lock_encoding in lock_encodings:
            match = all(key_height + lock_height <= MAX_HEIGHT
                        for key_height, lock_height in zip(
                            key_encoding, lock_encoding))
            if match:
                answer += 1

    print("ANSWER", answer)


def part_2(file):
    print("50 stars")


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
