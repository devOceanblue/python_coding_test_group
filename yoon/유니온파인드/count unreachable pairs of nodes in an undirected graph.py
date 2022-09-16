def solution(n, edges):
    def find(x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            return find(parent[x])
        return x

    # 두 원소가 속한 집합을 합치기
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [i for i in range(n)]

    for e in edges:
        union(e[0], e[1])

    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not find(i, j):
                result += 1
