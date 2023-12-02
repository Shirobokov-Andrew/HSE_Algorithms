import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs_find_cycle(start, end, adj, used):
    used[start] = True
    for v, _ in adj[start]:
        if not used[v]:
            dfs_find_cycle(v, end, adj, used)
        if v == end:
            return True
    return False


def main():
    N, M = map(int, input().split())
    adj = {i: set() for i in range(N)}
    for _ in range(M):
        v1, v2, w = map(int, input().split())
        adj[v2 - 1].add((v1 - 1, w))
    used = [False for _ in range(N)]
    dist = [float('-inf') for _ in range(N)]
    dist[0] = 0
    i = 0
    has_achievable_cycle = False
    while True:
        i += 1
        if i > 2000:
            for changing_v in changing_vertices:
                if dfs_find_cycle(N - 1, changing_v, adj, used):
                    has_achievable_cycle = True
                    break
            break
        changing_vertices = []
        for v in range(N):
            for u, w in adj[v]:
                if dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
                    changing_vertices.append(v)
        if not changing_vertices:
            break
    if dist[-1] == float('-inf'):
        print(':(')
    elif has_achievable_cycle:
        print(':)')
    else:
        print(dist[N - 1])


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
