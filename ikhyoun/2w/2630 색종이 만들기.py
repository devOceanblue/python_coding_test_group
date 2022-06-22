import sys
input = sys.stdin.readline

def colorPaper(n, nx, ny):
    global white, blue
    color = matrix[nx][ny]
    flag = True
    for x in range(nx, nx+n):
        for y in range(ny, ny + n):
            if matrix[x][y] != color:
                flag = False
                break
    
    if flag:
        if color == 0: white += 1
        else: blue += 1
    elif n > 0:
       colorPaper(n // 2, nx, ny)
       colorPaper(n // 2, nx + n//2, ny)
       colorPaper(n // 2, nx, ny + n//2)
       colorPaper(n // 2, nx + n//2, ny + n //2)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
white , blue = 0, 0
colorPaper(n, 0, 0)
print(white)
print(blue)