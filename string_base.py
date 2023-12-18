s = input()
n = len(s)
z = [0 for _ in range(n)]
z[0] = n
l, r = 0, 0
for i in range(1, n):
    z[i] = max(0, min(r - i, z[i - l]))
    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
        z[i] += 1
    if i + z[i] > r:
        l = i
        r = i + z[i]
result = 0
for i in range(1, n):
    if n - i == z[i]:
        result = i
        break
if result < n and result != 0:
    print(result)
else:
    print(n)
