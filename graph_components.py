import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs(v, adj,  used, counter, counter_list):
    used[v - 1] = True
    counter_list[v - 1] = counter
    for u in adj[v]:
        if not used[u - 1]:
            dfs(u, adj, used, counter, counter_list)


def main():
    N, M = map(int, input().split())
    adj = dict()
    for v in range(1, N + 1):
        adj.update({v: []})
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    used = [False for i in range(N)]
    counter = 0
    counter_list = [0 for i in range(N)]
    for v in adj:
        if not used[v - 1]:
            counter += 1
            dfs(v, adj, used, counter, counter_list)
    print(counter)
    print(*(i for i in counter_list))


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
