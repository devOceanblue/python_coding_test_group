def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        visited = set()
        nums_without_operator = int(str(N) * i)
        visited.add(nums_without_operator)

        for j in range(0, i - 1):
            for dp_1 in dp[j]:
                for dp_2 in dp[-j - 1]:
                    visited.add(dp_1 - dp_2)
                    visited.add(dp_1 + dp_2)
                    visited.add(dp_1 * dp_2)
                    if dp_2 != 0:
                        visited.add(dp_1 // dp_2)
        if number in visited:
            answer = i
            break
        dp.append(visited)
    return answer


if __name__ == "__main__":
    assert solution(5, 12) == 4
