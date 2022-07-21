from collections import deque
import sys

def solution(x, y):
    visited = [True] * 10000
    visited[x] = False
    queue = deque([(x, '')])
    while queue:
        num, path = queue.popleft()
        if num == y:
            return path
        
        length = len(str(num))
        
        value = (num * 2) % 10000
        if visited[value]:
            visited[value] = False
            queue.append((value, path + "D"))
            
        value = (num - 1) % 10000
        if visited[value]:
            visited[value] = False
            queue.append((value, path + "S"))
            
        if length < 4:
            value = num * 10
        else:
            value = (num % 1000) * 10 + num // 1000
        if visited[value]:
            visited[value] = False
            queue.append((value, path + "L"))
            
        value = (num % 10) * 1000 +  num // 10
                
        if visited[value]:
            visited[value] = False
            queue.append((value, path + "R"))

input = sys.stdin.readline

for _ in range(int(input())):
    A, B= map(int, input().split())
    print(solution(A, B))