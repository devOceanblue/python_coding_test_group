def solution(triangle):
    dp = [0 for _ in range(len(triangle)+1)]
    
    for row in triangle:
        col = len(row)
        for i in range(col-1,-1,-1):
            dp[i] = max(dp[i-1] + row[i],dp[i] + row[i])
    return max(dp)