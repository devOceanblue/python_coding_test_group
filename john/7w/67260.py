# https://school.programmers.co.kr/learn/courses/30/lessons/67260
import collections
import heapq

def solution(n, path, order):
    points = [set() for _ in range(n)]

    for i, j in path:
        points[i].add(j)
        points[j].add(i)
    
    def find_path(x, y):
        traced = set()
        def dfs(x, y):
            if x in traced:
                return False
            traced.add(x)
            if x == y:
                return True
            for i in points[x]:
                if i in traced:
                    continue
                if dfs(i, y):
                    return True
            traced.remove(x)
            return False
        dfs(x,y)
        return traced
    
    prohibits = set([y for _, y in order])
    heap = []
    first_point = 0
    for i, o in enumerate(order):
        visited = find_path(o[0], o[1])
        heapq.heappush(heap, (len(visited & prohibits), i, visited))
    flag = True

    first_point = 0
    while flag and heap:
        flag = False
        _, i, visited = heapq.heappop(heap)
        x, y = order[i]
        add_visited = find_path(first_point, x)
        if len(add_visited & prohibits) != 0:
            heapq.heappush(heap, (len(visited)+1, i, visited))
            flag = True
            continue
        visited.update(find_path(x, y))
        if len(visited & prohibits) == 1:
            prohibits -= visited
            flag = True
            first_point = y
            continue
        break
    return False if prohibits else True