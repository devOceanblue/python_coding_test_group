from collections import deque
import sys

input = sys.stdin.readline

def attachNumber(n, matrix):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    store = []
    
    for x in range(n):
        for y in range(n):
            if maxrix[x][y]:
                count = 1
                queue = deque([[x, y]])
                maxrix[x][y] = 0
                while queue:
                    x1, y1 = queue.popleft()
                    for i in range(4):
                        fx = x1 + dx[i]
                        fy = y1 + dy[i]
                        if 0 <= fx < n and 0 <= fy < n and maxrix[fx][fy]:
                            queue.append([fx, fy])
                            maxrix[fx][fy] = 0
                            count += 1
                store.append(count)
    
    store.sort()
    return store

n = int(input())
maxrix = [list(map(int, input()[:n])) for _ in range(n)]

array = attachNumber(n, maxrix)
print(len(array))
for item in array:
    print(item)