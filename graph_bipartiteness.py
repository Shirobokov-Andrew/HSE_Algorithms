import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs(v, adj, used, types):
    used[v - 1] = True
    for u in adj[v]:
        if not used[u - 1]:
            types[u - 1] = types[v - 1] ^ True
            dfs(u, adj, used, types)
        else:
            if types[u - 1] == types[v - 1]:
                global flag
                flag = False
                break

flag = True
def main():
    global flag
    N, M = map(int, input().split())
    adj = dict()
    for v in range(1, N + 1):
        adj.update({v: []})
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    used = [False for v in range(N)]
    for v in adj:
        if not used[v - 1]:
            types = [False for v in range(N)]
            dfs(v, adj, used, types)
            if not flag:
                break
    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
