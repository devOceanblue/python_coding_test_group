import sys

input = sys.stdin.readline


N,M = map(int,input().split())
G  = [] # N x N
dp = [[0 for _ in range(N+1)] for _ in range(N+1)] # (N+1) x (N+1)
"""
G           dp 
1 2 3 4     0 0 0 0 0
2 3 4 5     0 1 3 6 10
3 4 5 6     0 3 8 15 24
4 5 6 7     0 6 15 27 42
            0 10 24 42 64
"""
for _ in range(N):
    G.append(list(map(int,input().split())))

# dp »ý¼º
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + G[i][j]


for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result) 