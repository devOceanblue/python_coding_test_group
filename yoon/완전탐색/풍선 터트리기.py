from collections import deque

"""
인접한 두 풍선중 큰 풍선을 터트리는 행위 반복

[9,-1,-5]
[4,3,5,6]

기준점 기준 왼쪽 최솟값, 오른쪽 최솟값 구하고
만약 남은게 2개라면 무조건 True
만약 남은게 3개라면 나머지 두개보다 큰경우 False, 나머지 경우는 True
"""


def solution(a):
    result = [0 for _ in a]
    min_left, min_right = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < min_left:
            min_left = a[i]
            result[i] = 1
        if a[-1 - i] < min_right:
            min_right = a[-1 - i]
            result[-1 - i] = 1
    return sum(result)


if __name__ == "__main__":
    assert solution([9, -1, -5]) == 3
    assert solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]) == 6
