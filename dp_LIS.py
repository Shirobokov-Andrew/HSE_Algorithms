import bisect


n = int(input())
sequence = list(map(int, input().split()))
dp = [float('-inf')] + [float('inf')] * n
pos = [0] * (n + 1)
pos[0] = -1
prev = [0] * n
length = 0
for i in range(n):
    j = bisect.bisect_left(dp, sequence[i])
    dp[j] = sequence[i]
    pos[j] = i
    prev[i] = pos[j - 1]
    length = max(length, j)
answer = []
p = pos[length]
while p != -1:
    answer.append(sequence[p])
    p = prev[p]
answer.reverse()
print(len(answer))
print(*answer)
