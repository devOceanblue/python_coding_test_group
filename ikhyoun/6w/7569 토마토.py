import sys
from collections import deque
input = sys.stdin.readline

def solution(boxs, location):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    dz = [-1, 1]
    days = 0
    queue = location
    
    while queue:
        z, y, x = queue.popleft()
        value = boxs[z][y][x]

        for i in range(4):
            fx = x + dx[i]
            fy = y + dy[i]
            if 0 <= fx < N and 0 <= fy < M and boxs[z][fy][fx] == 0:
                boxs[z][fy][fx] = value + 1
                queue.append((z, fy, fx))
        
        for i in range(2):
            fz = z + dz[i]
            if 0 <= fz < H and boxs[fz][y][x] == 0:
                boxs[fz][y][x] = value + 1
                queue.append((fz, y, x))
    
    max_value = 0
    
    for box in boxs:
        for row in box:
            if 0 in row: return -1
            now_max_value = max(row)
            if max_value < now_max_value:
                max_value = now_max_value
                
    return max_value - 1

N, M, H = map(int, input().split())
tensor = []
location = deque([])

for z in range(H):
    metrix = []
    for y in range(M):
        vector = list(map(int, input().split()))
        for x, value in enumerate(vector):
            if value == 1:
                location.append((z, y, x))
        metrix.append(vector)
    tensor.append(metrix)
    
print(solution(tensor, location))