"""
time python3 23.py
python3 23.py  0.23s user 0.02s system 95% cpu 0.258 total
"""
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    connections = set()
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            connections.add(tuple(line.split("-")))
    graph = collections.defaultdict(set)
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)
    return graph, connections


def part_1(file):
    graph, connections = read_input(file)

    def count_set_of_3(nodes):
        res = 0
        for first_node in nodes:
            for second_node in graph[first_node] & nodes:
                res += len(graph[first_node] & graph[second_node] & nodes)
        return res // 6

    non_t_nodes = set(node for node in graph if not node.startswith("t"))
    answer = count_set_of_3(set(graph)) - count_set_of_3(non_t_nodes)
    print("ANSWER", answer)


def part_2(file):
    graph, connections = read_input(file)

    def bron_kerbosch(current_clique, candidate_nodes, excluded_nodes):
        """
        Recursive function to find all maximal cliques using the Bron-Kerbosch algorithm.
        """
        if not candidate_nodes and not excluded_nodes:
            nonlocal max_clique
            if len(current_clique) > len(max_clique):
                max_clique = current_clique
        else:
            for node in list(candidate_nodes):
                bron_kerbosch(current_clique.union({node}),
                              candidate_nodes.intersection(graph[node]),
                              excluded_nodes.intersection(graph[node]))
                candidate_nodes.remove(node)
                excluded_nodes.add(node)

    max_clique = set()
    bron_kerbosch(set(), set(graph), set())
    answer = ",".join(sorted(max_clique))
    print("ANSWER", answer)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(SAMPLE_FILE)
    part_2(INPUT_FILE)
