T = int(input())

for _ in range(T):
    n = int(input())
    dp = [0] * (n+3)
    dp[0] = 1

    for i in range(1, n+1):
        dp[i] += dp[i-1]
        dp[i] += dp[i-2]
        dp[i] += dp[i-3]
    print(dp[n])