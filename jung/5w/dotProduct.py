# 대수적으로 내적은 두 수열의 해당 항목의 곱 의 합입니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer


# 다른 사람의 풀이

def solution2(a, b):
    return sum([x*y for x, y in zip(a,b)])

solution3 = lambda x, y: sum(a*b for a, b in zip(x, y))