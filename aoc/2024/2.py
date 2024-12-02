from collections import Counter
import bisect

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"

def read_input(file):
    reports = []
    with open(file, "r") as f:
        for line in f.readlines():
            levels = list(map(int, line.split()))
            reports.append(levels)
    return reports

def is_safe_report(report):
    is_inc = True
    is_dec = True
    adj_diff = True
    for i in range(len(report) - 1):
        if report[i+1] <= report[i]:
            is_inc = False
        if report[i+1] >= report[i]:
            is_dec = False
        if abs(report[i+1] - report[i]) > 3:
            adj_diff = False
    return (is_inc or is_dec) and (adj_diff)


def part_1(file):
    reports = read_input(file)
    safe_count = sum(1 if is_safe_report(report) else 0 for report in reports)
    print(f"ANSWER: {safe_count}")

def part_2(file):
    reports = read_input(file)
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
        else:
            for del_idx in range(len(report)):
                new_report = report[:del_idx] + report[del_idx+1:]
                if is_safe_report(new_report):
                    safe_count += 1
                    break
    print(f"ANSWER: {safe_count}")



if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
