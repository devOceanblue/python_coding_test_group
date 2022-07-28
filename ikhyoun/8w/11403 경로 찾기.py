import sys
input = sys.stdin.readline

def solution(n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj[i][k] and adj[k][j]:
                    adj[i][j] = 1

n = int(input())

adj = []

for i in range(n):
    array = list(map(int, input().split()))
    adj.append(array)
            
solution(n)

for item in adj:
    print(' '.join(map(str, item)))