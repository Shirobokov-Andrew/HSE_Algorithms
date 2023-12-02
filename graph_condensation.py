import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs_order(v, adj, used, order):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs_order(u, adj, used, order)
    order.append(v)


def dfs_component(v, adj_rev,  colors, color):
    colors[v] = color
    for u in adj_rev[v]:
        if colors[u] == -1:
            dfs_component(u, adj_rev, colors, color)


def main():
    N, M = map(int, input().split())
    adj = dict()
    adj_rev = dict()
    for v in range(N):
        adj.update({v: set()})
        adj_rev.update({v: set()})
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj[v1 - 1].add(v2 - 1)
        adj_rev[v2 - 1].add(v1 - 1)

    used = [False for i in range(N)]
    order = []
    colors = [-1 for v in range(N)]
    color = 0
    condensed_edges = set()
    for v in adj:
        if not used[v]:
            dfs_order(v, adj, used, order)
    for v in reversed(order):
        if colors[v] == -1:
            color += 1
            dfs_component(v, adj_rev, colors, color)
    for v in adj:
        for u in adj[v]:
            if colors[v] != colors[u]:
                condensed_edges.add((colors[v], colors[u]))
    print(len(condensed_edges))


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
