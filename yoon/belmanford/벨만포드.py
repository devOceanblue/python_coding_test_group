n, m = map(int, input().split())

graph = []

for i in range(m):
    u, v, w = list(map(int, input().split()))
    graph.append([u, v, w])


def BellmanFord(src):
    dist = [float("inf") for i in range(n + 1)]
    dist[src] = 0

    for i in range(n - 1):
        for u, v, w in graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    cycle = 0
    for u, v, w in graph:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            cycle = 1
            break
    if cycle == 0:
        print("Distance from source vertex", src)
        print("Vertex \t Distance from source")
        for i in range(1, len(dist)):
            print(i, "\t", dist[i])


if __name__ == "__main__":
    BellmanFord(1)
