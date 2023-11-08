string1 = input()
string2 = input()
length1 = len(string1)
length2 = len(string2)
dp = [[0 for i in range(length1 + 1)] for j in range(length2 + 1)]
for i in range(length2 + 1):
    for j in range(length1 + 1):
        if i == 0 or j == 0:
            dp[i][j] = i + j
            continue
        if string1[j - 1] == string2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
print(dp[-1][-1])
