from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n, m = numCourses, len(prerequisites)

        graph = [[] for i in range(n + 1)]
        indegree = [0] * (n + 1)

        for p in prerequisites:
            graph[p[0] + 1].append(p[1] + 1)
            indegree[p[1] + 1] += 1

        def topology_sort():
            result = []
            q = deque()

            for i in range(1, n + 1):
                if indegree[i] == 0:
                    q.append(i)
            while q:
                now = q.popleft()
                result.append(now)

                for i in graph[now]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
            if len(result) == numCourses:
                return True
            else:
                return False

        return topology_sort()
