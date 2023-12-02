import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs(v, adj, used, parent):
    global cycle_flag, cycle_start, cycle_end
    if cycle_flag:
        return
    used[v - 1] = 1
    for u in adj[v]:
        if used[u - 1] == 0:
            parent[u - 1] = v - 1
            dfs(u, adj, used, parent)
        elif used[u - 1] == 1:
            cycle_start = u - 1
            cycle_end = v - 1
            cycle_flag = True
            break
    used[v - 1] = 2


cycle_flag = False
cycle_start = -1
cycle_end = -1


def main():
    global cycle_flag, cycle_start, cycle_end
    N, M = map(int, input().split())
    adj = dict()
    for v in range(1, N + 1):
        adj.update({v: set()})
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj[v1].add(v2)

    used = [0 for v in range(N)]
    parent = [-1 for v in range(N)]
    for v in adj:
        if cycle_flag:
            break
        if used[v - 1] == 0:
            dfs(v, adj, used, parent)
    if not cycle_flag:
        print("NO")
    cycle = []
    if cycle_flag:
        k = cycle_end
        while k != cycle_start:
            cycle.append(k + 1)
            k = parent[k]
        print("YES")
        print(cycle_start + 1, *reversed(cycle))


if __name__ == '__main__':
    sys.setrecursionlimit(110000)
    threading.stack_size(200000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
