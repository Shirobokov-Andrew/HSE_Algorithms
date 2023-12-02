def find_v_min(used, dist):
    v_min = 0
    min_dist = float('inf')
    for v in range(len(used)):
        if dist[v] < min_dist and not used[v]:
            min_dist = dist[v]
            v_min = v
    return v_min


N = int(input())
adj_matrix = []
for _ in range(N):
    adj_matrix.append(list(map(int, input().split())))
max_distance = [0] * N
for v in range(N):
    dist = [float('inf') for _ in range(N)]
    dist[v] = 0
    used = [False for _ in range(N)]
    for _ in range(N):
        v = find_v_min(used, dist)
        if dist[v] == float('inf'):
            break
        used[v] = True
        for u, w in enumerate(adj_matrix[v]):
            if not used[u] and w != -1:
                dist[u] = min(dist[u], dist[v] + w)
    max_distance[v] = max(dist)
print(max(max_distance))  # diameter
print(min(max_distance))  # radius
