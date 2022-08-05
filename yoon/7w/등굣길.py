def solution(m, n, puddles):
    puddles = set(list(map(tuple, puddles)))
    queue = [(1, 1)]
    count = 0
    while queue:
        cur = queue.pop()
        if cur == (m, n):
            count %= 1000000007
            count += 1
            continue
        if cur[0] + 1 <= m and (cur[0] + 1, cur[1]) not in puddles:
            queue.append((cur[0] + 1, cur[1]))
        if cur[1] + 1 <= n and (cur[0], cur[1] + 1) not in puddles:
            queue.append((cur[0], cur[1] + 1))
    return count % 1000000007
