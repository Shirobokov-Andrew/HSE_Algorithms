import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def euler(v, adj, N):
    while adj[v]:
        u = adj[v].pop()
        adj[u].remove(v)
        euler(u, adj, N)
        if v != N:
            print(v + 1, end=' ')
        else:
            print()


def main():
    N, M = map(int, input().split())
    adj = {v: set() for v in range(N + 1)}
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj[v1 - 1].add(v2 - 1)
        adj[v2 - 1].add(v1 - 1)
    for v in range(N):
        if len(adj[v]) % 2 == 1:
            adj[v].add(N)
            adj[N].add(v)
    if not adj[N]:
        print(1)
        print(1, end=' ')
        euler(0, adj, N)
    else:
        print(len(adj[N]) // 2)
        euler(N, adj, N)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(30000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
