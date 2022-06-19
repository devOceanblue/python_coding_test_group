from collections import defaultdict


def solution(n, adjacent_matrix):
    def get_adjacent_graph(adjacent_matrix):
        adjacent_graph = defaultdict(list)
        for i in range(len(adjacent_matrix)):
            for j in range(len(adjacent_matrix[i])):
                if adjacent_matrix[i][j] == 1:
                    adjacent_graph[i].append(j)
        return adjacent_graph

    count = 0
    visited = set()
    computer_map = get_adjacent_graph(adjacent_matrix)

    def dfs(visited, start, graph, depth):
        nonlocal count
        for node in graph[start]:
            if node not in visited:
                if depth == 1:
                    count += 1
                visited.add(node)
                dfs(visited, node, graph, depth + 1)

    for key in computer_map.keys():
        dfs(visited, key, computer_map, 1)
    return count
