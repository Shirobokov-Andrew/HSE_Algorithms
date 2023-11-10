brackets = input()
n = len(brackets)
dp = [[0 for i in range(n)] for j in range(n)]
for r in range(n):
    for l in range(r, -1, -1):
        if r == l:
            dp[r][l] = 1
        else:
            if brackets[l] == '{' and brackets[r] == '}' or brackets[l] == '(' and brackets[r] == ')' or\
                    brackets[l] == '[' and brackets[r] == ']':
                min_num = dp[r - 1][l + 1]
            else:
                min_num = min(dp[r - 1][l], dp[r][l + 1]) + 1
            for i in range(l, r):
                min_num = min(min_num, dp[i][l] + dp[r][i + 1])
            dp[r][l] = min_num
print(n - dp[n - 1][0])
