import sys
input = sys.stdin.readline
    
dp = [0, 1, 1, 1]

for i in range(4, 101):
    dp.append(dp[i - 2] + dp[i - 3])

for _ in range(int(input())):
    print(dp[int(input())])