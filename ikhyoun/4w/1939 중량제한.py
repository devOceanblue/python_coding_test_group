from collections import deque
import sys

input = sys.stdin.readline

def solution(N, adj, start_node, end_node):
    def bfs(n):
        visited = [False for _ in range(N + 1)]
        visited[start_node] = True
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            for bridge, weight  in adj[node]:
                if visited[bridge] == False and n < weight:
                    visited[bridge] = True
                    queue.append(bridge)
                    
        return visited[end_node]
    
    start, end = 1, int(1e9+1)
    while start<= end:
        middle = (start + end) // 2
        if bfs(middle): start = middle + 1
        else: end = middle - 1
    return start
    

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A].append((B, C))
    adj[B].append((A, C))
    
start_node, end_node = map(int, input().split())
print(solution(N, adj, start_node, end_node))