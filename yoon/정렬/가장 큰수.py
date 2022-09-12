import functools

"""
아이디어:
두 수를 더했을때 더 큰 숫자가 되도록 custom_sort를 하는 함수를 만들어 정렬
"""


def solution(numbers):
    def compare_numbers(i, j):
        if int(i + j) > int(j + i):
            return 1
        elif int(i + j) < int(j + i):
            return -1
        else:
            return 0

    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(compare_numbers), reverse=True)
    result = "".join(numbers)
    return result if result[0] != "0" else "0"
