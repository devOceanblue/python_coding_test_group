from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                graph.append(
                    (
                        i,
                        j,
                        abs(points[i][0] - points[j][0])
                        + abs(points[i][1] - points[j][1]),
                    )
                )
        graph.sort(key=lambda x: x[2])  # 가중치로 간선 정렬 (정점1, 정점2, 가중치)

        mst = []
        n = len(points)  # 정점 개수
        p = [0]  # 상호배타적 집합

        for i in range(1, n + 1):
            p.append(i)  # 각 정점 자신이 집합의 대표

        def find(u):
            if u != p[u]:
                p[u] = find(p[u])  # 경로압축
            return p[u]

        def union(u, v):
            root1 = find(u)
            root2 = find(v)
            p[root2] = root1  # 임의로 root2가 root1의 부모

        tree_edges = 0  # 간선 개수
        mst_cost = 0  # 가중치 합

        while True:
            if tree_edges == n - 1:
                break
            u, v, wt = graph.pop(0)
            if find(u) != find(v):  # u와 v가 서로 다른 집합에 속해 있으면
                union(u, v)
                mst.append((u, v))
                mst_cost += wt
                tree_edges += 1
        return mst_cost
