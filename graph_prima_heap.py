import sys
import threading
from concurrent.futures import ThreadPoolExecutor
import heapq


def main():
    n, m = map(int, input().split())
    adj = {v: set() for v in range(n)}
    for _ in range(m):
        v1, v2, w = map(int, input().split())
        adj[v1 - 1].add((v2 - 1, w))
        adj[v2 - 1].add((v1 - 1, w))
    tree_vertices = set()
    tree_vertices.add(0)
    heap = []
    heapq.heapify(heap)
    for u, w in adj[0]:
        heapq.heappush(heap, (w, u))
    tree_weight = 0
    while len(heap):
        w, u = heapq.heappop(heap)
        if u in tree_vertices:
            continue
        else:
            tree_vertices.add(u)
            tree_weight += w
            for v, ww in adj[u]:
                if v not in tree_vertices:
                    heapq.heappush(heap, (ww, v))
    print(tree_weight)




if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
