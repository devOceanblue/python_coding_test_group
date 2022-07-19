# 가장 큰 수
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    # numbers = [str(number) for number in numbers]

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda number: number * 3, reverse=True)

    return str(int(''.join(numbers)))