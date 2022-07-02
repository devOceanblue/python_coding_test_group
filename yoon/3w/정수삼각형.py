def solution(triangle):
    d = [[0] * len(triangle) for _ in range(len(triangle))]
    answer = d[0][0] = triangle[0][0]
    height = len(triangle)
    for i in range(1, height):
        for j in range(0, i + 1):
            if j == 0:
                d[i][j] = d[i - 1][j] + triangle[i][j]
            elif j == i:
                d[i][j] = d[i - 1][j - 1] + triangle[i][j]
            else:
                d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + triangle[i][j]
            answer = max(answer, d[i][j])
    return answer
