def solution(a, b, g, s, w, t):
    start = 0
    end = (10 ** 9) * (10 ** 5) * 4
    answer = float("inf")

    while start <= end:
        mid = (start + end) // 2
        accumulated_gold = 0
        accumulated_silver = 0
        total_weight = 0

        for idx, time in enumerate(t):
            cnt = (mid - time) // (time * 2) + 1

            if cnt * w[idx] > g[idx]:
                accumulated_gold += g[idx]
            if cnt * w[idx] <= g[idx]:
                accumulated_gold += cnt * w[idx]
            if cnt * w[idx] > s[idx]:
                accumulated_silver += s[idx]
            if cnt * w[idx] <= s[idx]:
                accumulated_silver += cnt * w[idx]
            if s[idx] + g[idx] < cnt * w[idx]:
                total_weight += s[idx] + g[idx]
            if s[idx] + g[idx] >= cnt * w[idx]:
                total_weight += cnt * w[idx]
        if accumulated_gold >= a and accumulated_silver >= b and total_weight >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer
