"""
아이디어:
제곱근을 시작점으로 하면 모두 돌 필요가 없음
"""


import math
from math import sqrt


def solution(brown, yellow):
    max_val = math.ceil(sqrt(yellow))
    for x in range(max_val, yellow + 1):
        for y in range(max_val, -1, -1):
            if x >= y and x * y == yellow and 2 * (x + y) + 4 == brown:
                return [x + 2, y + 2]


if __name__ == "__main__":
    assert solution(8, 1) == [3, 3]
