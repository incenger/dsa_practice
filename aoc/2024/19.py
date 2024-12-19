"""
time python3 19.py
python3 19.py  0.05s user 0.02s system 86% cpu 0.079 total
"""
import functools

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    patterns = []
    towels = []
    with open(file, "r") as f:
        is_pattern = True
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            if is_pattern:
                patterns = [pattern.strip() for pattern in line.split(",")]
                is_pattern = False
            else:
                towels.append(line)
    return patterns, towels


def build_trie(patterns):
    pattern_trie = {}
    for pattern in patterns:
        cur = pattern_trie
        for color in pattern:
            cur = cur.setdefault(color, {})
        # Mark a pattern
        cur['#'] = True
    return pattern_trie


def part_1(file):
    patterns, towels = read_input(file)

    pattern_trie = build_trie(patterns)

    @functools.cache
    def check(towel):
        if not towel:
            return True

        trie_cur = pattern_trie
        for idx, color in enumerate(towel):
            trie_cur = trie_cur.get(color, None)
            if trie_cur is None:
                return False
            if '#' in trie_cur and check(towel[idx + 1:]):
                return True
        return False

    answer = 0
    for towel in towels:
        if check(towel):
            answer += 1
    print("ANSWER", answer)


def part_2(file):
    patterns, towels = read_input(file)

    pattern_trie = build_trie(patterns)

    @functools.cache
    def count(towel):
        if not towel:
            return 1
        options = 0
        trie_cur = pattern_trie
        for idx, color in enumerate(towel):
            trie_cur = trie_cur.get(color, None)
            if trie_cur is None:
                break
            if '#' in trie_cur:
                options += count(towel[idx + 1:])
        return options

    answer = 0
    for towel in towels:
        answer += count(towel)
    print("ANSWER", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
