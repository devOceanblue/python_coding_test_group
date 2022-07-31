import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def solution(board, lader, snake):
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for i in range(1, 7):
            moveTo = node + i
            if 0 < moveTo <= 100 and not visited[moveTo]:
                if moveTo in lader.keys():
                    moveTo = lader[moveTo]
                
                if moveTo in snake.keys():
                    moveTo = snake[moveTo]
                
                if not visited[moveTo]:
                    queue.append(moveTo)
                    board[moveTo] = board[node] + 1
                    visited[moveTo] = True

    return board[100]                
    
board = [0] * 101
visited = [False] * 101

lader = defaultdict(int)

snake = defaultdict(int)

N, M = map(int, input().split())

for _ in range(N):
    x, y = map(int, input().split())
    lader[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y    
    
print(solution(board, lader, snake))