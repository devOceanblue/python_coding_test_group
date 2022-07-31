import sys
input = sys.stdin.readline

def solution(x, y, value, count = 0):
    global max_value
    if max_value >= value + max_val * (3 - count): return
    if count == 3:
        max_value = max(max_value, value)
        return
    else:
        for k in range(4):
            fx = x + dx[k]
            fy = y + dy[k]
            if 0 <= fx < N and 0 <= fy < M and visited[fx][fy]:
                if count == 1:
                    visited[fx][fy] = False
                    solution(x, y, value + board[fx][fy], count + 1 )
                    visited[fx][fy] = True
                visited[fx][fy] = False
                solution(fx, fy, value + board[fx][fy], count + 1)
                visited[fx][fy] = True
        
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
visited = [[True] * M  for __ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]
max_value = 0
max_val = max(map(max, board))

for i in range(N):
    for j in range(M):
        visited[i][j] = False
        solution(i, j, board[i][j])
        visited[i][j] = True

print(max_value)