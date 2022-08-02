import heapq


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
    graph = {}
    for i in range(1, n + 1):
        graph[i] = {}

    for v in vertex:
        graph[v[0]][v[1]] = 1
        graph[v[1]][v[0]] = 1

    result = dijkstra(graph, 1)
    maximum = max(result.values())
    cnt = 0
    for v in result.values():
        if v == maximum:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
