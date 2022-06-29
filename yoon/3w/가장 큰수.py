import functools


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
