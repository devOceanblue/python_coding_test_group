from collections import deque
import sys
import copy
input = sys.stdin.readline

def solution(n, session, flag):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    count = 0
    for x in range(n):
        for y in range(n):
            node = session[x][y]
            if node:
                count += 1
                location = deque([(x, y)])
                session[x][y] = False
                while location:
                    x1, y1 = location.popleft()
                    for i in range(4):
                        fx = x1 + dx[i]
                        fy = y1 + dy[i]
                        if flag and node in ('R', 'G'):
                            q = 0 <= fx < n and 0 <= fy < n and session[fx][fy] in ('R', 'G')
                        else: 
                            q = 0 <= fx < n and 0 <= fy < n and session[fx][fy] == node
                        if  q:
                            session[fx][fy] = False
                            location.append((fx, fy))
    return count

N = int(input())
matrix1 = []
for _ in range(N):
    row = list(input()[:N])
    matrix1.append(row)

matrix2 = copy.deepcopy(matrix1)

print(solution(N, matrix1, False), solution(N, matrix2, True))