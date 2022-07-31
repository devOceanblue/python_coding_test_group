import sys
from collections import deque

def solution(sea, x, y, size):
    move = 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    exe = 0
    sea[y][x] = 0
    
    # 먹이 찾기
    def eat(x, y):
        visited = [[False] * n for _ in range(n)]
        visited[y][x] = True
        move_cnt = [[0] * n for _ in range(n)]
        queue = deque([(x, y)])
        fishes = []
        while queue:
            nx, ny = queue.popleft()
            for i in range(4):
                fx = nx + dx[i]
                fy = ny + dy[i]
                if 0 <= fx < n and 0 <= fy < n and not visited[fy][fx] and sea[fy][fx] <= size:
                    now_count = move_cnt[ny][nx] +1
                    move_cnt[fy][fx] = now_count
                    visited[fy][fx] = True
                    queue.append((fx, fy))
                    if 0 < sea[fy][fx] < size:
                        fishes.append((fx, fy, now_count))
        
        return sorted(fishes, key = lambda fish: (fish[2], fish[1], fish[0]))
            
    
    while 1:
        fish = eat(x, y)
        if len(fish) == 0:
            return move
        else:
            sea[y][x] = 0
            x, y, cnt = fish[0]
            move += cnt
            exe += 1
            if exe == size:
                exe  = 0
                size += 1
            sea[y][x] = 0
            
# 초기 세팅
n = int(input())

x = 0
y = 0
sea = []

# 세팅하면서 상어 위치 저장
for i in range(n):
    array = list(map(int, input().split()))
    sea.append(array)
    for j in range(n):
        if array[j] == 9:
            x, y = j, i

print(solution(sea, x, y, 2))