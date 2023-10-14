def take_first(elem):
    return elem[0]


def take_second(elem):
    return elem[1]


n, k = (map(int, input().split()))
commands = [tuple(map(int, input().split())) for i in range(n)]
commands.sort(key=take_second)
commands.sort(key=take_first, reverse=True)
print(commands.count(commands[k-1]))
