S, n = (map(int, input().split()))
weights = list(map(int, input().split()))
dp = [[False for i in range(S + 1)] for j in range(n + 1)]
dp[0][0] = True
for k in range(1, n + 1):
    for w in range(S + 1):
        if w - weights[k - 1] < 0:
            dp[k][w] = dp[k - 1][w]
        else:
            dp[k][w] = dp[k - 1][w] or dp[k - 1][w - weights[k - 1]]
for w in range(S, -1, -1):
    if dp[-1][w]:
        print(w)
        break
