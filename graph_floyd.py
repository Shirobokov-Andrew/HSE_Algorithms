n, m, k = map(int, input().split())
dist = [[float('-inf') for i in range(n)] for j in range(n)]
edges = []
next_v = [[None for i in range(n)] for j in range(n)]
for _ in range(m):
    v1, v2, w = map(int, input().split())
    dist[v1 - 1][v2 - 1] = w
    next_v[v1 - 1][v2 - 1] = v2 - 1
    edges.append((v1 - 1, v2 - 1))
cities = list(map(int, input().split()))
for v in range(n):
    dist[v][v] = 0
    next_v[v][v] = v
for i in range(n):
    for u in range(n):
        for v in range(n):
            if dist[u][v] < dist[u][i] + dist[i][v]:
                dist[u][v] = dist[u][i] + dist[i][v]
                next_v[u][v] = next_v[u][i]
path = [cities[0] - 1]
for i in range(1, k):
    city1 = cities[i - 1] - 1
    city2 = cities[i] - 1
    if dist[city1][city1] > 0:
        print('infinitely kind')
        exit(0)
    c = city1
    while c != city2:
        if dist[c][c] > 0:
            print('infinitely kind')
            exit(0)
        c = next_v[c][city2]
        path.append(c)
print(len(path) - 1)
for i in range(len(path) - 1):
    print(edges.index((path[i], path[i + 1])) + 1, end=' ')
