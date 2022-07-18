# 첫 생각
슬라이싱 이용하여 계산하려고 했음 
a ~ b 까지의 누적합 `sum(A[a:b+1])` 
M만큼 반복하므로
시간복잡도 : O(NM)

# 다른 방법을 생각
a ~ b 까지의 누적합 : A[a] + A[a+1] + ... A[b-1] + A[b]  


# 반복적인 풀이를 최소화  
S[n] : 0번째 인덱스부터 n번째 인덱스 까지의 합
S[b] = A[0]+ A[1] + ... + A[a-1]+ A[a] + ... + A[b]  
S[a-1] = A[0]+ A[1] + ....+ A[a-1]  

A[a] + ....A[b] = S[b] - S[a-1]



``` python
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr_sum = [0 for _ in range(N+1)]
for i in range(N):
    arr_sum[i+1] = arr_sum[i] + arr[i] # 누적합

for _ in range(M):
    start,end = map(int,input().split())
    result = arr_sum[end] - arr_sum[start-1]
    print(result)
```



# 2차원 문제
S[a][b] = (0,0) 에서 (a,b) 까지의 합(직사각형)
prefix_sum을 이용하여 계산해보자

# 아이디어
<img src = "https://user-images.githubusercontent.com/62232531/177738341-1c58417b-7533-4538-b537-4646fa4f356a.png">




# 그림
<img src ="https://user-images.githubusercontent.com/62232531/177486930-c23f9fc9-7c87-4de5-8206-b0ddfde402c5.png">


``` python
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

# dp 생성
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + G[i][j]


for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result) 
```


# 응용 문제 (백준 / 골드 3 )
https://www.acmicpc.net/problem/10986
