import sys
from collections import deque
input = sys.stdin.readline

def mazeSearch(n, m, matrix):

    #방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    queue = deque([[0, 0]]) # 출발 지점
    
    while queue:
        y, x = queue.popleft()
        value = matrix[y][x]
        for i in range(4):
            fx = x + dx[i]
            fy = y + dy[i]
            
            if (0 <= fx < m) and (0 <= fy < n) and (matrix[fy][fx] == 1):
                queue.append([fy, fx])
                matrix[fy][fx] = value + 1

    return matrix[n-1][m-1]

n, m = map(int, input().split())

matrix = [list(map(int, input()[:m])) for _ in range(n)]

print(mazeSearch(n, m, matrix))