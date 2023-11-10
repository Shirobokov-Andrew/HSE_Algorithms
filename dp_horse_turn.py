n = int(input())
adj = ((4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), None, (0, 1, 7), (2, 6), (1, 3), (2, 4))
dp = [[0] + [1] * 7 + [0] + [1] if i == 0 else [0] * 10 for i in range(n)]
for k in range(1, n):
    for p in range(10):
        if p == 5:
            continue
        else:
            for i in adj[p]:
                dp[k][p] += dp[k - 1][i]
print(sum(dp[-1]) % 10 ** 9)
