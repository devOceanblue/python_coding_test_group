def soulution(n):
    
    dp = [0] * (10 ** 6 + 1)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4, n+1):
        dp[i] = dp[i-1]
        if i % 2 == 0: 
            dp[i] = min(dp[i], dp[i//2])
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3])
        dp[i] += 1
    
    return dp[n]

print(soulution(int(input())))