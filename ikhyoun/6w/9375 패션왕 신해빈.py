import sys
input = sys.stdin.readline

def solution(n, items):
    count = 1
    for kind, close in items.items():
        count *= len(items[kind]) + 1
    return count - 1
    

for _ in range(int(input())):
    close = {}
    n = int(input())
    for _ in range(n):
        item, kind = input().split()
        if kind in close:
            close[kind].append(item)
        else:
            close[kind] = [item]
    print(solution(n, close))