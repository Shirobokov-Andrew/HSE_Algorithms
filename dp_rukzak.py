n, S = (map(int, input().split()))
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))
dp = [[0 for i in range(S + 1)] for j in range(n + 1)]
for k in range(1, n + 1):
    for w in range(1, S + 1):
        if w < weights[k - 1]:
            dp[k][w] = dp[k - 1][w]
        else:
            dp[k][w] = max(dp[k - 1][w], dp[k - 1][w - weights[k - 1]] + costs[k - 1])
items = []
k = n
w = S
while k != 0:
    if dp[k][w] == dp[k - 1][w]:
        k -= 1
    else:
        items.append(k)
        w -= weights[k - 1]
        k -= 1
items.reverse()
print(len(items))
print(*items)
