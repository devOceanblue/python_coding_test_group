import sys
from collections import deque

def labyrinthSearch(n, m, maze):
    
    #방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    queue = deque([[0, 0]]) # 출발 지점
    
    while queue:
        y, x = queue.popleft()
        value = maze[y][x]
        for i in range(4):
            fx = x + dx[i]
            fy = y + dy[i]
    
            if (0 <= fx < m) and (0 <= fy < n) and (maze[fy][fx] == 1):
                queue.append([fy, fx])
                maze[fy][fx] = value + 1
    
    return maze[n-1][m-1]

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input()[:m])) for _ in range(n)]


print(labyrinthSearch(n, m , matrix))