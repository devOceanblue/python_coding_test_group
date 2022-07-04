"""
아이디어:
다이나믹 프로그래밍 => 점화식 dp[i] = max(dp[i-1], dp[i-2] + money[i])
첫번째 집을 터는 경우와 두번째집을 터는 경우를 시작점으로 정함

원형태로 집들이 이어져있으므로 첫번째 집을 터는 경우 마지막집을 털지 못하므로 dp1[-2]를 리턴
두번째집을 터는 경우 마지막집을 리턴 dp2[-1]


"""


def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)

    dp1[0] = money[0]
    for i in range(1, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    dp2[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[-2], dp2[-1])
