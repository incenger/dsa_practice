from collections import defaultdict


def read_file(file):
    with open(file, "r") as f:
        lines = [l.strip() for l in f.readlines()]
    edges = [l.split("-") for l in lines]

    return edges


def is_lowercase(s):
    return s.lower() == s


def part_1(edges):
    small_caves = set()
    big_caves = set()
    # Edge_id: 0 - > start, N -> end
    edge2id = {
        "start": 0,
    }

    graph = defaultdict(list)

    for u, v in edges:
        if u != "end" and u not in edge2id:
            edge2id[u] = len(edge2id)

        if v != "end" and v not in edge2id:
            edge2id[v] = len(edge2id)

    edge2id["end"] = len(edge2id)
    end_id = edge2id["end"]

    for u, v in edges:
        graph[edge2id[u]].append(edge2id[v])
        graph[edge2id[v]].append(edge2id[u])

    visited = [False] * len(edge2id)
    is_small_case = [False] * len(edge2id)

    for case, case_id in edge2id.items():
        if 0 < case_id < end_id and is_lowercase(case):
            is_small_case[case_id] = True

    total_path = 0

    def dfs(v):
        nonlocal total_path

        if v == end_id:
            total_path += 1
            return

        for u in graph[v]:
            if u != 0 and not visited[u]:
                if is_small_case[u]:
                    visited[u] = True
                dfs(u)
                if is_small_case[u]:
                    visited[u] = False

    # print(edge2id)
    # print(is_small_case)
    dfs(0)
    visited[0] = True
    return total_path


def part_2(edges):
    # Edge_id: 0 - > start, N -> end
    edge2id = {
        "start": 0,
    }

    graph = defaultdict(list)

    for u, v in edges:
        if u != "end" and u not in edge2id:
            edge2id[u] = len(edge2id)

        if v != "end" and v not in edge2id:
            edge2id[v] = len(edge2id)

    edge2id["end"] = len(edge2id)
    end_id = edge2id["end"]

    for u, v in edges:
        graph[edge2id[u]].append(edge2id[v])
        graph[edge2id[v]].append(edge2id[u])

    visited = [False] * len(edge2id)
    is_small_case = [False] * len(edge2id)

    for case, case_id in edge2id.items():
        if 0 < case_id < end_id and is_lowercase(case):
            is_small_case[case_id] = True

    total_path = 0

    def dfs(v, repeat):
        nonlocal total_path

        if v == end_id:
            total_path += 1
            return

        for u in graph[v]:
            if u == 0:
                continue
            if not visited[u]:
                if is_small_case[u]:
                    visited[u] = True
                dfs(u, repeat)
                visited[u] = False
            elif visited[u] and repeat:
                dfs(u, False)

    dfs(0, True)
    return total_path


if __name__ == "__main__":
    edges = read_file("input.txt")
    total_path = part_2(edges)

    print(total_path)
