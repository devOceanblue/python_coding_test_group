def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    routes_length = len(routes)
    checked = [0] * routes_length

    for i in range(routes_length):
        if checked[i] == 0:
            camera = routes[i][1]  # 진출 지점에 카메라를 갱신
            answer += 1
        for j in range(i + 1, routes_length):
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
    return answer


if __name__ == "__main__":
    assert solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]) == 2
