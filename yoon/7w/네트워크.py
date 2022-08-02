def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return
    parent[x] = y


def solution(n, computers):
    result = set()
    parent = [i for i in range(n)]
    for i in range(len(computers)):
        for j in range(i):
            if computers[i][j] == 1:
                union(parent, i, j)

    for i in range(n):
        result.add(find(parent, i))
    return len(result)
