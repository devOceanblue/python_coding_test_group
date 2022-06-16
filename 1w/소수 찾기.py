from itertools import permutations


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    count = 0
    visited = set()

    for i in range(1, len(numbers) + 1):
        temp = set(permutations(numbers, i))
        for r in temp:
            num = int("".join(r))
            if is_prime(num) and num > 1 and num not in visited:
                visited.add(num)
                count += 1
    return count


if __name__ == "__main__":
    print(solution("011"))
