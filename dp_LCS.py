N = int(input())
S = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
dp = [[0 for i in range(M + 1)] for j in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if S[i - 1] == T[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
