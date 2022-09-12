"""
로봇청소기는 시작할때 방향(수평,수직)을 설정할수있다.
로봇청소기는 일렬로 외곽을 방문하고 다음 외곽으로 이동한다.
이때 로봇청소기가 방문한 순서를 2차원배열로 표현하기

입력값: n(배열의크기), horizontal(방향)

무조건 수평 출발인 경우에 대해서만 생각
horizontal인 경우 수평, 아닌경우 수직으로 한칸 이동하고 BFS 탐색


"""


def solution(n, horizontal):
    visited = [[0, 0]]
    if horizontal == 1:
        start = [0, 1]
    else:
        start = [1, 0]
    queue = [start]
    visited.append(start)
    robot_dir = -horizontal

    for k in range(1, n):
        while queue:
            cur = queue.pop()
            if (
                0 <= cur[0] + 1 <= n - 1
                and 0 <= cur[1] <= n - 1
                and cur[0] + 1 <= k
                and cur[1] <= k
                and [cur[0] + 1, cur[1]] not in visited
            ):
                queue.append([cur[0] + 1, cur[1]])
                visited.append([cur[0] + 1, cur[1]])
            elif (
                0 <= cur[0] - 1 <= n - 1
                and 0 <= cur[1] <= n - 1
                and cur[0] - 1 <= k
                and cur[1] <= k
                and [cur[0] - 1, cur[1]] not in visited
            ):
                queue.append([cur[0] - 1, cur[1]])
                visited.append([cur[0] - 1, cur[1]])
            elif (
                0 <= cur[0] <= n - 1
                and 0 <= cur[1] + 1 <= n - 1
                and cur[0] <= k
                and cur[1] + 1 <= k
                and [cur[0], cur[1] + 1] not in visited
            ):
                queue.append([cur[0], cur[1] + 1])
                visited.append([cur[0], cur[1] + 1])
            elif (
                0 <= cur[0] <= n - 1
                and 0 <= cur[1] - 1 <= n - 1
                and cur[0] <= k
                and cur[1] - 1 <= k
                and [cur[0], cur[1] - 1] not in visited
            ):
                queue.append([cur[0], cur[1] - 1])
                visited.append([cur[0], cur[1] - 1])
        if robot_dir == -1:
            queue.append([visited[-1][0] + 1, visited[-1][1]])
            visited.append([visited[-1][0] + 1, visited[-1][1]])
        else:
            queue.append([visited[-1][0], visited[-1][1] + 1])
            visited.append([visited[-1][0], visited[-1][1] + 1])
        robot_dir *= -1
    return visited[:-1]


if __name__ == "__main__":
    print(solution(4, 1))
