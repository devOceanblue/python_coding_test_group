import heapq


def solution(land, height):
    N = len(land)

    # 방문 여부를 체크하는 2차원 배열
    visited = [[False for _ in range(N)] for _ in range(N)]
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 큐
    queue = []

    visit_count = 0
    max_count = N * N
    value = 0

    # 탐색 시작 지점을 큐에 넣는다.
    queue.append((0, 0, 0))

    while visit_count < max_count:
        # 사다리비용, x좌표, y좌표
        val, x, y = heapq.heappop(queue)

        # 이미 방문한 곳이라면 건너뛴다.
        if visited[x][y]:
            continue
        visited[x][y] = True

        visit_count += 1
        value += val

        # 현재 칸의 높이
        current_height = land[x][y]

        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 다음 칸의 높이
            next_height = land[nx][ny]

            # 현재 칸과 다음 칸의 높이 차이가 height보다 크다면 사다리가 필요한 시점
            if abs(next_height - current_height) > height:
                heapq.heappush(
                    queue, (abs(next_height - current_height), nx, ny)
                )  # (사다리비용, x좌표, y좌표)
            # 사다리가 필요하지 않은 시점은 사다리비용을 0으로 처리
            # 다음 반복문에서 value += 0 이기 때문에 결과값에 영향을 미치지 않음
            else:
                heapq.heappush(queue, (0, nx, ny))
    return value
