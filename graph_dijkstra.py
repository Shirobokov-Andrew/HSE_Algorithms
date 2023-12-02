def find_v_min(N, used, dist):
    v_min = 0
    min_dist = float('inf')
    for v in range(N):
        if dist[v] < min_dist and not used[v]:
            min_dist = dist[v]
            v_min = v
    return v_min


N, S, F = map(int, input().split())
S = S - 1
F = F - 1
adj_matrix = []
for _ in range(N):
    adj_matrix.append(list(map(int, input().split())))
dist = [float('inf') for _ in range(N)]
dist[S] = 0
used = [False for _ in range(N)]
for _ in range(N):
    v = find_v_min(N, used, dist)
    if dist[v] == float('inf'):
        break
    used[v] = True
    for u, w in enumerate(adj_matrix[v]):
        if not used[u] and w != -1:
            dist[u] = min(dist[u], dist[v] + w)

if dist[F] != float('inf'):
    print(dist[F])
else:
    print(-1)
