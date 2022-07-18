import sys
input = sys.stdin.readline

def solution(N, C, routers):
    gap = [routers[i] - routers[i - 1] for i in range(1, N)]
    min_gap, max_gap = min(gap), routers[-1] - routers[0]
    while min_gap <= max_gap:
        middle = (min_gap + max_gap) // 2
        value = routers[0]
        count = 1
        for i in range(1, len(routers)):
            if (routers[i] - value >= middle):
                count += 1
                value = routers[i]
        if count < C: max_gap = middle - 1
        else: min_gap = middle + 1
    return max_gap

N, C = map(int, input().split())
routers = [int(input()) for _ in range(N)]
routers.sort()

print(solution(N, C, routers))