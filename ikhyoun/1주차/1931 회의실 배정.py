import sys
input = sys.stdin.readline

data = []

N = int(input())
for _ in range(N):
    s, e = map(int, input().split())
    data.append([s, e])

data.sort(key = lambda x: (x[1], x[0]))
start = data[0][1]
count = 1
for i in range(1, len(data)):
    if start <= data[i][0]:
        count +=1
        start = data[i][1]

print(count)