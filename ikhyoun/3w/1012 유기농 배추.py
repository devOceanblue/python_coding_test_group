import sys
from collections import deque
input = sys.stdin.readline

def solution(matrix, points ,m, n, k):
    
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    count = 0
    while points:
        location = points.popleft()
        queue = deque([location])
        if visited[location]:
            count += 1
            visited[location] = False
            while queue:             
                point = queue.popleft()
                for i in range(4):
                    fx, fy = point[0] + dx[i], point[1] + dy[i]
                    if (fx, fy) in points and visited[(fx, fy)]: 
                        visited[(fx, fy)] = False
                        queue.append((fx, fy))
    return count
    

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    points = deque()
    visited = {}
    for _ in range(k):
        y, x = map(int, input().split())
        points.append((x, y))
        visited[(x, y)] = True
        matrix[x][y] = 1
    print(solution(matrix, points, m, n, k))
