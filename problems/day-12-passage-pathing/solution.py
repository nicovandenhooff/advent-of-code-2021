# Advent of Code 2021
# Day 12: Part 1 and Part 2
# Author: Nico Van den Hooff

import networkx as nx


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    return data


def get_directed_graph(data):
    """Creates a directed graph based on the given nodes and edges"""

    G = nx.DiGraph()
    nodes = set()
    edges = [edges.split("-") for edges in data]

    # creates set of nodes
    for edge in edges:
        for node in edge:
            nodes.add(node)

    # adds nodes to graphs
    for node in nodes:
        G.add_node(node)

    # creates directed edges
    for edge in edges:
        if edge[0] == "start" or edge[1] == "end":
            G.add_edge(edge[0], edge[1])
        elif edge[0] == "end" or edge[1] == "start":
            G.add_edge(edge[1], edge[0])
        else:
            G.add_edge(edge[0], edge[1])
            G.add_edge(edge[1], edge[0])

    return G


def get_caves(G):
    """Creates two sets for small and big caves"""
    small_caves = set()
    big_caves = set()

    for node in G.nodes:
        if node in ["start", "end"]:
            # not a cave
            continue
        elif node.islower():
            small_caves.add(node)
        else:
            big_caves.add(node)

    return small_caves, big_caves


def backtrack(G, node, path, paths, small_caves):
    """Backtracking algorithm to find all paths visiting small caves at most once"""

    if node == "end":
        paths.append(path)

    for neighbor in G.neighbors(node):
        if neighbor in small_caves and neighbor in path:
            continue

        current_path = path + [neighbor]
        backtrack(G, neighbor, current_path, paths, small_caves)


def part_1(data):

    paths = []
    path = ["start"]

    G = get_directed_graph(data)
    small_caves, big_caves = get_caves(G)
    backtrack(G, "start", path, paths, small_caves)
    solution1 = len(paths)

    return solution1


def part_2():
    pass


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    # solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    # print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-12-passage-pathing/input.txt"
    main(path)
