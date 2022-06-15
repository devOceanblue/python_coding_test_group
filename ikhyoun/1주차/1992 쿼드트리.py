import sys

def cutting(x, y, k):
    flag = True
    start = matrix[x][y]
    for i in range(x, x+k):
        for j in range(y, y+k):
            if matrix[i][j] != start:
                flag = False
                break
        if flag == False: break
    if flag:
        return str(start)
    else:
        result = ""
        if k == 2:
            for i in range(x, x+k):
                for j in range(y, y+k):
                    result += str(matrix[i][j])
        else:
            value = k //2
            for i in range(2):
                for j in range(2):
                    result +=  cutting(x + i * value, y + j * value, value)
        return "(" + result + ")"
    
input = sys.stdin.readline

matrix = []
n = int(input())
for _ in range(n):
    matrix.append(list(map(int, input()[:-1])))
    
print(cutting(0, 0, n))