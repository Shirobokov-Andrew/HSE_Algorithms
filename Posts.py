n, m = (map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
prefixes = [a[0]]
for i in range(1, n):
    prefixes.append(a[i] + prefixes[i-1])
del a
i = 0
j = 0
k = 0
while i < len(prefixes):
    for j in range(k, m):
        if b[j] <= prefixes[i]:
            if i == 0:
                print(1, b[j])
                j += 1
            else:
                print(i + 1, b[j] - prefixes[i - 1])
                j += 1
        else:
            k = j
            break
    if j == m:
        break
    i += 1
