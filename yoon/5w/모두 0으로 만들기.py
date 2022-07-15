from collections import defaultdict

answer = 0


def dfs(x, a, tree, visited):
    global answer
    visited[x] = 1
    for y in tree[x]:
        if not visited[y]:
            a[x] += dfs(y, a, tree, visited)
    answer += abs(a[x])
    return a[x]


def solution(a, edges):
    global answer
    if sum(a) != 0:
        return -1
    tree = defaultdict(list)
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)
    visited = [0 for _ in range(len(a))]
    dfs(x=0, a=a, tree=tree, visited=visited)
    return answer


if __name__ == "__main__":
    assert solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]) == 9
