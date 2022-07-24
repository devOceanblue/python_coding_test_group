import sys
input = sys.stdin.readline

def solution(N, M, x, y):
        k = x
        while k <= N * M:
                if (k - x) % N == 0 and (k - y) % M == 0:
                        return k
                k += N
        return -1

for _ in range(int(input())):
        N, M, x, y = map(int, input().rstrip().split())
        print(solution(N, M, x, y))