import re
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    rules = []
    updates = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                page_1, page_2 = map(int, line.split("|"))
                rules.append((page_1, page_2))
            else:
                updates.append(list(map(int, line.split(","))))
    return rules, updates


def part_1(file):
    rules, updates = read_input(file)
    answer = 0
    for update in updates:
        ordered = True
        position = {page: idx for idx, page in enumerate(update)}
        for x, y in rules:
            if x in position and y in position and position[x] > position[y]:
                ordered = False
                break
        if ordered:
            answer += update[len(update) // 2]
    print("ANSWER:", answer)


def topo_sort(rules, update):
    pages = set(update)
    graph = collections.defaultdict(list)
    in_degree = collections.defaultdict(int)
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1

    queue = collections.deque([page for page in pages if in_degree[page] == 0])
    order = []
    while queue:
        page = queue.popleft()
        order.append(page)
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order


def part_2(file):
    """
    Filter rules applied for the current update and perform topo sort
    """
    rules, updates = read_input(file)
    answer = 0
    for update in updates:
        sorted_update = topo_sort(rules, update)
        if update != sorted_update:
            answer += sorted_update[len(sorted_update) // 2]
    print("ANSWER:", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
