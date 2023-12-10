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
    used = [False for _ in range(n * m)]
    banned = set(banned_vertices)
    if dfs(0, adj, used, banned):
        print(-1)
    else:
        l = 0
        r = k
        while r - l > 1:
            used = [False for _ in range(n * m)]
            median = (l + r) // 2
            banned = set(banned_vertices[0:median])
            if dfs(0, adj, used, banned):
                l = median
            else:
                r = median
        print(l + 1)


if __name__ == '__main__':
    main()
