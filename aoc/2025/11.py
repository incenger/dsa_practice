import collections
import functools

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    graph = collections.defaultdict(list)
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            source, dests = line.split(":")
            graph[source].extend(dests.strip().split())
    return graph


def count_path(graph, node, dest):

    @functools.cache
    def dfs(node):
        if node == dest:
            return 1
        path = 0
        for neighbor in graph[node]:
            path += dfs(neighbor)
        return path

    return dfs(node)


def part_1(file):
    graph = read_input(file)
    answer = count_path(graph, "you", "out")
    print(f"Part 1: {answer}")


def part_2(file):
    graph = read_input(file)
    paths = [["svr", "dac", "fft", "out"], ["svr", "fft", "dac", "out"]]
    answer = 0
    for path in paths:
        path_count = 1
        for i in range(len(path) - 1):
            path_count *= count_path(graph, path[i], path[i + 1])
        answer += path_count
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
