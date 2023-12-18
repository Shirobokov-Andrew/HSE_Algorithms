import sys
import threading
from concurrent.futures import ThreadPoolExecutor


class Trie:
    def __init__(self,
                 char: str = None,
                 parent: 'Trie' = None,
                 suf_link=None):
        self.move = dict()
        self.char = char
        self.parent = parent
        self.suf_link = suf_link
        self.terminal = False
        self.color = 0

    def add_word(self, word: str):
        node = self
        for char in word:
            if char not in node.move:
                node.move[char] = Trie(char=char, parent=node)
            node = node.move[char]
        node.terminal = True


def bfs(trie):
    q = []
    q.append(trie)
    while q:
        v = q.pop(0)
        for kid in v.move:
            q.append(v.move[kid])
            build_suf_link(trie, v.move[kid])
            u = v.move[kid].suf_link
            if u.terminal:
                v.move[kid].terminal = True


def build_suf_link(trie: 'Trie', c: 'Trie'):
    p = c.parent
    x = c.char
    v = p.suf_link
    while v != -1:
        if x in v.move:
            c.suf_link = v.move[x]
            return
        v = v.suf_link
    c.suf_link = trie


def build_move(trie: 'Trie', c: 'Trie', char: str):
    state = c
    if state == trie and char not in state.move:
        c.move[char] = trie
        return
    if char in state.move:
        return
    if char not in state.move:
        state = state.suf_link
        while state != -1:
            if char in state.move:
                c.move[char] = state.move[char]
                return
            state = state.suf_link
        if state == -1:
            if char not in trie.move:
                c.move[char] = trie
            else:
                c.move[char] = trie.move[char]


def dfs(trie: 'Trie', v: 'Trie'):
    v.color = 1
    for char in ['0', '1']:
        build_move(trie, v, char)
        u = v.move[char]
        if not u.terminal:
            if u.color == 0:
                dfs(trie, u)
            elif u.color == 1:
                print('TAK')
                sys.exit(0)
    v.color = 2


def main():
    n = int(input())
    trie = Trie(suf_link=-1)
    for _ in range(n):
        word = input()
        trie.add_word(word)
    bfs(trie)
    dfs(trie, trie)
    print('NIE')


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(100000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
