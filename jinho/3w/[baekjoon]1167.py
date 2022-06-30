import sys
input = sys.stdin.readline
from collections import deque



n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n):
    start , *others  = map(int,input().split()) 
    others = others[:-1]
    for i in range(0,len(others),2):
        G[start].append((others[i],others[i+1]))

def bfs(node):
    visited = [False for _ in range(n+1)]
    Q = deque()
    Q.append((0,node))
    visited[node] = True
    result = [0,0]
    while Q:
        dist , current = Q.popleft()
        for next,extra_dist in G[current]:
            if not visited[next]:
                visited[next] =True
                Q.append((dist+extra_dist,next))
                if result[0] < dist+extra_dist:
                    result[0] = dist+extra_dist
                    result[1] = next
    return result
result = 0
first_dist,first_node = bfs(1)
second_dist,_ = bfs(first_node)
result = max(result,first_dist,second_dist)
print(second_dist)