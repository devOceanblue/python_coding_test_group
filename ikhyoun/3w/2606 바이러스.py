import sys

def solution(grape):
    stack = [1]
    virus = []
    while stack:
        node = stack.pop()
        if node not in virus:
            virus.append(node)
            stack.extend(grape[node])
    return len(virus) - 1

data = {i : [] for i in range(1, int(input()) + 1)}

for _ in range(int(input())):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)



print(solution(data))