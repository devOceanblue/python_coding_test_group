from collections import defaultdict


def solution(n, results):
    """
    i에게 이긴노드와 진노드의 합이 같으면 순위가 결정되었다는걸 아이디어로 삼아서 푸는 알고리즘
    """
    answer = 0
    wins = defaultdict(set)
    loses = defaultdict(set)

    for win, lose in results:
        wins[lose].add(win)
        loses[win].add(lose)

    for i in range(1, n + 1):
        for win in wins[i]:
            loses[win].update(loses[i])
        for lose in loses[i]:
            wins[lose].update(wins[i])

    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
