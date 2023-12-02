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


def solve_2_sat(N, M):
    if M == 0:
        for i in range(N):
            print(0)
        return
    adj = {v: set() for v in range(2 * N)}
    adj_rev = {v: set() for v in range(2 * N)}
    used = [False for v in range(2 * N)]
    order = []
    color = 0
    colors = [-1 for v in range(2 * N)]
    for _ in range(M):
        i1, e1, i2, e2 = map(int, input().split())
        if e1 == 1 and e2 == 1:
            adj[2 * i1 + 1].add(2 * i2)
            adj[2 * i2 + 1].add(2 * i1)
            adj_rev[2 * i2].add(2 * i1 + 1)
            adj_rev[2 * i1].add(2 * i2 + 1)
        elif e1 == 1 and e2 == 0:
            adj[2 * i1 + 1].add(2 * i2 + 1)
            adj[2 * i2].add(2 * i1)
            adj_rev[2 * i2 + 1].add(2 * i1 + 1)
            adj_rev[2 * i1].add(2 * i2)
        elif e1 == 0 and e2 == 1:
            adj[2 * i1].add(2 * i2)
            adj[2 * i2 + 1].add(2 * i1 + 1)
            adj_rev[2 * i2].add(2 * i1)
            adj_rev[2 * i1 + 1].add(2 * i2 + 1)
        elif e1 == 0 and e2 == 0:
            adj[2 * i1].add(2 * i2 + 1)
            adj[2 * i2].add(2 * i1 + 1)
            adj_rev[2 * i2 + 1].add(2 * i1)
            adj_rev[2 * i1 + 1].add(2 * i2)
    for v in adj:
        if not used[v]:
            dfs_order(v, adj, used, order)
    for v in reversed(order):
        if colors[v] == -1:
            color += 1
            dfs_component(v, adj_rev, colors, color)
    for v in range(N):
        if colors[2 * v] > colors[2 * v + 1]:
            print(1, end='')
        else:
            print(0, end='')
    print('')


def main():
    while True:
        N_and_M = sys.stdin.readline().split()
        if not N_and_M:
            break
        N, M = map(int, N_and_M)
        solve_2_sat(N, M)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
