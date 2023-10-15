from collections import deque


n, k = [int(i) for i in input().split()]
a_numbers = deque([int(i) for i in input().split()])
for i in range(k):
    if len(a_numbers) == 1:
        x = a_numbers.pop()
        a_numbers.append(0)
        break
    else:
        x = a_numbers.popleft()
        y = a_numbers.pop()
        if x < y:
            a_numbers.append(y)
            a_numbers.append((x + y) & ((1 << 30) - 1))
        else:
            a_numbers.appendleft(x)
            a_numbers.appendleft((y - x) & ((1 << 30) - 1))
for i in range(len(a_numbers)):
    print(a_numbers.popleft(), end=' ')
