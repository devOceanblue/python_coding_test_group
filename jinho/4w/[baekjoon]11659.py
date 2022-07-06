import sys
input = sys.stdin.readline



N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr_sum = [0 for _ in range(N+1)]
for i in range(N): 
    arr_sum[i+1] = arr_sum[i] + arr[i] # 누적 합

for _ in range(M):
    start,end = map(int,input().split())
    result = arr_sum[end] - arr_sum[start-1]
    print(result)
