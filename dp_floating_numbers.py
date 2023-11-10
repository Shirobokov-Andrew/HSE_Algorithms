N = int(input())
dp = [[0] * 10 if i != 0 else [1] * 10 for i in range(N)]
for k in range(1, N):
    for p in range(10):
        if p == 9:
            dp[k][p] = dp[k - 1][p] + dp[k - 1][p - 1]
        elif p == 0:
            dp[k][p] = dp[k - 1][p] + dp[k - 1][p + 1]
        else:
            dp[k][p] = dp[k - 1][p] + dp[k - 1][p + 1] + dp[k - 1][p - 1]
print(sum(dp[-1][1:]))