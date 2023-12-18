def dfs(v, adj, used, banned_vertices):
    used[v] = True
    if v == len(used) - 1:
        return True
    for u in adj[v].difference(banned_vertices):
        if not used[u]:
            if dfs(u, adj, used, banned_vertices):
                return True
    return False


def main():
    n, m, k = map(int, input().split())
    adj = {i: set() for i in range(n * m)}
    for i in range(n * m):
        if (i + 1) % m == 0 and i != n * m - 1:
            adj[i].add(i + m)
        elif n * m - m <= i:
            if i != n * m - 1:
                adj[i].add(i + 1)
        else:
            adj[i].add(i + 1)
            adj[i].add(i + m)
    banned_vertices = []
    for _ in range(k):
        x, y = map(int, input().split())
        banned_vertices.append((x - 1) * m + (y - 1))
    l = -1
    r = k + 1
    while r - l > 1:
        median = (l + r) // 2
        if dfs(0, adj, [False for _ in range(n * m)], set(banned_vertices[:median])):
            l = median
        else:
            r = median
    if r == k + 1:
        print(-1)
    else:
        print(r)


if __name__ == '__main__':
    main()
