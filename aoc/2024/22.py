"""
time python3 22.py
python3 22.py  3.92s user 0.70s system 88% cpu 5.228 total
"""
import functools
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    secrets = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                secrets.append(int(line))
    return secrets


@functools.cache
def compute_next_secret(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


def part_1(file):
    secrets = read_input(file)
    NUM_GEN = 2000
    answer = 0
    for secret in secrets:
        new_secret = secret
        for _ in range(NUM_GEN):
            new_secret = compute_next_secret(new_secret)
        answer += new_secret
    print("ANSWER", answer)


def part_2(file):
    secrets = read_input(file)
    NUM_GEN = 2000

    windows = collections.defaultdict(int)
    for secret in secrets:
        seen = set()
        window = collections.deque()
        current_secret = secret
        for _ in range(NUM_GEN):
            next_secret = compute_next_secret(current_secret)
            current_price = current_secret % 10
            next_price = next_secret % 10
            window.append(next_price - current_price)
            if len(window) == 4:
                window_id = tuple(window)
                if window_id not in seen:
                    windows[window_id] += next_price
                    seen.add(window_id)
                window.popleft()
            current_secret = next_secret

    answer = max(windows.values())
    print("ANSWER", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
