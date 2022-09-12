import collections
import math


# 그룹화를 시킬때 사다리 없이 방문할 수 있는 칸을 bfs로 탐색한다.
def bfs(land, height, groups, x, y, group_number):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = collections.deque([(x, y)])
    groups[x][y] = group_number

    while queue:
        now = queue.popleft()

        # 상, 하, 좌, 우 이동
        for i in range(4):
            new_x = now[0] + move[i][0]
            new_y = now[1] + move[i][1]

            # 범위 밖을 벗어나는 경우는 pass
            if (
                new_x < 0
                or new_y < 0
                or new_x >= len(groups)
                or new_y >= len(groups[0])
                or groups[new_x][new_y] != 0
            ):
                continue

            # 사다리 없이 방문 가능한 경우에는 큐에 추가하고, 해당 칸에 그룹번호를 입력시킨다.
            if abs(land[new_x][new_y] - land[now[0]][now[1]]) <= height:
                queue.append((new_x, new_y))
                groups[new_x][new_y] = group_number


# 그룹과 그룹 사이의 가중치의 최솟값을 구한다.
def get_groups_wieghts(land, groups, height):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 그룹과 그룹 사이의 가중치를 저장할 딕셔너리
    # 기본값으로 inf를 둔다.
    # 키 : (그룹a, 그룹b)
    # 값 : 최소 가중치
    weights = collections.defaultdict(lambda: math.inf)

    for i in range(len(groups)):
        for j in range(len(groups[0])):
            now = groups[i][j]
            for dx, dy in move:
                new_x, new_y = i + dx, j + dy

                # 범위를 벗어나는 경우 pass
                if (
                    new_x < 0
                    or new_y < 0
                    or new_x >= len(groups)
                    or new_y >= len(groups[0])
                    or groups[new_x][new_y] == now
                ):
                    continue

                dist = abs(land[new_x][new_y] - land[i][j])

                # 그룹과 그룹 사이 놓을 수 있는 사다리 중 가장 적은 비용을 저장
                weights[(now, groups[new_x][new_y])] = min(
                    dist, weights[(now, groups[new_x][new_y])]
                )

    return weights


# 유니온파인드 알고리즘의 find 메소드
# root[x]의 값이 본인이 아니라는 것은
# 종속되어 있는(=이어져있는) 다른 노드가 존재함을 의미
def find(x, root):
    if x == root[x]:
        return x
    else:
        r = find(root[x], root)
        root[x] = r
        return r


# 유니온파인드 알고리즘의 union 메소드
# x와 y의 각각의 뿌리를 찾아서 하나로 합쳐준다.
def union(x, y, root):
    x_root = find(x, root)
    y_root = find(y, root)
    root[y_root] = x_root


# 크루스칼 알고리즘
def kruskal(group_weights, groups):
    sum = 0
    roots = {_: _ for _ in range(1, groups)}  # {1:1, 2:2, 3:3 ... }

    for (x, y), value in group_weights:
        if find(x, roots) != find(y, roots):
            sum += value
            union(x, y, roots)
        if len(roots.items()) == 1:
            return sum
    return sum


def solution(land, height):
    answer = 0
    row = len(land)
    col = len(land[0])

    groups = [[0 for _ in range(col)] for _ in range(row)]

    group_number = 1
    for i in range(row):
        for j in range(col):
            if groups[i][j] == 0:
                bfs(land, height, groups, i, j, group_number)
                group_number += 1

    groups_weights = get_groups_wieghts(land, groups, height)

    # 가중치 값이 작은 순서로 정렬
    groups_weights = sorted(groups_weights.items(), key=lambda x: x[1])

    answer = kruskal(groups_weights, group_number)
    return answer
