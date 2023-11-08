N = int(input())
dp = [0] * N
for i in range(1, N):
    if (i + 1) % 2 == 0 and (i + 1) % 3 == 0:
        dp[i] = min(dp[i // 2], dp[i // 3], dp[i - 1]) + 1
    elif (i + 1) % 2 == 0 and (i + 1) % 3 != 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    elif (i + 1) % 2 != 0 and (i + 1) % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1
print(dp[-1])
i = N
numbers = []
while i != 1:
    if i % 2 == 0 and dp[i // 2 - 1] == dp[i - 1] - 1:
        i = i // 2
        numbers.append(i)
    elif i % 3 == 0 and dp[i // 3 - 1] == dp[i - 1] - 1:
        i = i // 3
        numbers.append(i)
    else:
        i = i - 1
        numbers.append(i)
print(*reversed(numbers), N)
