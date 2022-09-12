import collections

"""
아이디어:
1. 방문한 점이 이미 똑같은 경로로 방문한적이 있다면 사이클을 만들지 않는다.
2. 다른 경로로 방문했다면 재방문했다면 사이클을 만든다.
3. 모래시계형태를 가지는 경우 위의 조건으로 검색하지 못하므로 그래프의 크기를 두배로 늘려서 탐색한다.

"""


def solution(arrows):
    result = 0
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    start = (0, 0)

    visited_node = collections.defaultdict(int)
    path_of_visited_node = collections.defaultdict(int)

    queue = collections.deque([start])
    for i in arrows:
        for _ in range(2):
            next = (start[0] + move[i][0], start[1] + move[i][1])
            queue.append(next)
            start = next
    start = queue.popleft()
    visited_node[start] = 1

    while queue:
        next = queue.popleft()
        if visited_node[next] == 1:
            if path_of_visited_node[(start, next)] == 0:
                result += 1
        else:
            visited_node[next] = 1
        path_of_visited_node[(start, next)] = 1
        path_of_visited_node[(next, start)] = 1
        start = next
    return result


if __name__ == "__main__":
    print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
