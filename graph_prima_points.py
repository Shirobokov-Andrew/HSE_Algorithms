import sys
import threading
from concurrent.futures import ThreadPoolExecutor
import math


def find_new_pair(N, used, adj_matrix, tree_vertices):
    min_dist = float('inf')
    pair_candidate = (0, 0)
    for v in tree_vertices:
        for u in range(N):
            if not used[u] and adj_matrix[v][u] < min_dist:
                min_dist = adj_matrix[v][u]
                pair_candidate = (v, u)
    return pair_candidate


def main():
    N = int(input())
    used = [False for _ in range(N)]
    adj_matrix = [[-1 for i in range(N)] for j in range(N)]
    points = []
    tree = []
    tree_vertices = set()
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    for i in range(N):
        for j in range(N):
            adj_matrix[i][j] = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
    used[0] = True
    tree_vertices.add(0)
    while len(tree_vertices) != N:
        new_pair = find_new_pair(N, used, adj_matrix, tree_vertices)
        tree.append(new_pair)
        tree_vertices.add(new_pair[1])
        used[new_pair[1]] = True
    sum_distance = 0
    for pair in tree:
        sum_distance += adj_matrix[pair[0]][pair[1]]
    print(sum_distance)
    print(len(tree))
    for pair in tree:
        print(pair[0] + 1, pair[1] + 1)




if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
