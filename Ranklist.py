n, k = (map(int, input().split()))
commands = [tuple(map(int, input().split())) for i in range(n)]
commands.sort(key=lambda x: x[0])
commands.sort(key=lambda x: x[1], reverse=True)
print(commands.count(commands[k-1]))
