import heapq
from collections import defaultdict


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


def solution(n, vertex):
    graph = defaultdict(dict)
    for start, dest in vertex:
        graph[start][dest] = 1
        graph[dest][start] = 1
    result = dijkstra(graph, 1)

    values = list(result.values())
    max_value = max(values)
    count = 0
    for v in values:
        if v == max_value:
            count += 1
    return count


if __name__ == "__main__":
    assert solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3
