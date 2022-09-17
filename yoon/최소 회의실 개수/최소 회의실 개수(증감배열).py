import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, 1])
    arr.append([e, -1])
arr.sort()

cnt = 0
_max = 0
for x, v in arr:
    cnt += v
    if v == 1:
        _max = max(_max, cnt)

print(_max)
