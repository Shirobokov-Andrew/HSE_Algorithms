alpha = input()
beta = input()
concat = beta + '#' + alpha
pref = [-1 for _ in range(len(concat) + 1)]
positions = []
for i in range(1, len(concat) + 1):
    k = pref[i - 1]
    while k != -1 and concat[k] != concat[i - 1]:
        k = pref[k]
    pref[i] = k + 1
for i in range(len(concat) + 1):
    if pref[i] == len(beta):
        positions.append(i - 2 * len(beta))
print(len(positions))
print(*positions)
