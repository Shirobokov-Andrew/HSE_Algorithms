import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def join(x, y, parents, rank, experience):
    px, _ = get_par_exp(x, experience, parents)
    py, _ = get_par_exp(y, experience, parents)
    if px == py:
        return
    if rank[px] > rank[py]:
        px, py = py, px
    if rank[px] == rank[py]:
        rank[py] += 1
    parents[px] = py
    experience[px] -= experience[py]


def add_exp(x, exp, parents, experience):
    px, _ = get_par_exp(x, experience, parents)
    experience[px] += exp


def get_par_exp(x, experience, parents):
    if parents[x] == x:
        return x, 0
    px, px_exp = get_par_exp(parents[x], experience, parents)
    experience[x] += px_exp
    parents[x] = px
    return parents[x], experience[x]


def main():
    n, m = map(int, input().split())
    parents = [i for i in range(n)]
    rank = [0 for i in range(n)]
    experience = [0 for i in range(n)]
    input_list = []
    for _ in range(m):
        input_list.append(input())
    for q in input_list:
        query = q.split()
        if query[0] == 'join':
            x = int(query[1]) - 1
            y = int(query[2]) - 1
            join(x, y, parents, rank, experience)
        elif query[0] == 'add':
            x = int(query[1]) - 1
            exp = int(query[2])
            add_exp(x, exp, parents, experience)
        elif query[0] == 'get':
            x = int(query[1]) - 1
            px, _ = get_par_exp(x, experience, parents)
            if x != px:
                print(experience[x] + experience[px])
            else:
                print(experience[x])


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
