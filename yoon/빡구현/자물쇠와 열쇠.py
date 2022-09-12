def solution(a, b, g, s, w, t):
    start = 0
    end = (10 ** 9) * (10 ** 5) * 4
    answer = float("inf")

    while start <= end:
        mid = (start + end) // 2
        accumulated_gold = 0
        accumulated_silver = 0
        total_weight = 0

        for i, time in enumerate(t):
            cnt = (mid - time) // (time * 2) + 1
            if cnt * w[i] > g[i]:
                accumulated_gold += g[i]
            if cnt * w[i] <= g[i]:
                accumulated_gold += cnt * w[i]
            if cnt * w[i] > s[i]:
                accumulated_silver += s[i]
            if cnt * w[i] <= s[i]:
                accumulated_silver += cnt * w[i]
            if s[i] + g[i] < cnt * w[i]:
                total_weight += s[i] + g[i]
            if s[i] + g[i] >= cnt * w[i]:
                total_weight += cnt * w[i]
        if accumulated_gold >= a and accumulated_silver >= b and total_weight >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer
