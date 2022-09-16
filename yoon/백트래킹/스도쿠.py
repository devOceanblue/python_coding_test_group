import sys

# 가로 체크
def horizontal(x, val):
    if val in arr[x]:
        return False
    return True


# 세로 체크
def vertical(y, val):
    for i in range(9):
        if val == arr[i][y]:
            return False
    return True


# 3x3 체크
def bythree(x, y, val):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == arr[nx + i][ny + j]:
                return False
    return True


def dfs(index):
    if index == len(zeros):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()
        sys.exit(0)  # 하나의 답만 출력해야하므로 시스템을 종료한다 return으로 하면 오답이됨
    # 1부터 9까지 탐색하며 답이 될 수 있으면 넣고 다음 dfs로 이동
    for i in range(1, 10):
        nx = zeros[index][0]
        ny = zeros[index][1]
        if horizontal(nx, i) and vertical(ny, i) and bythree(nx, ny, i):
            arr[nx][ny] = i
            dfs(index + 1)
            arr[nx][ny] = 0


arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

zeros = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
dfs(0)
