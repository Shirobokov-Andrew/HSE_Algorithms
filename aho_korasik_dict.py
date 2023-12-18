class Trie:
    def __init__(self,
                 char: str = None,
                 parent: 'Trie' = None,
                 suf_link=None):
        self.move = dict()
        self.char = char
        self.parent = parent
        self.suf_link = suf_link
        self.word = '#'

    def add_string(self, string: str):
        node = self
        for char in string:
            if char not in node.move:
                node.move[char] = Trie(char=char, parent=node, suf_link=None)
            node = node.move[char]
        node.word = string


def bfs(trie):
    q = []
    q.append(trie)
    while q:
        v = q.pop(0)
        for kid in v.move:
            q.append(v.move[kid])
            build_suf_link(trie, v.move[kid])


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


text = input()
m = int(input())
trie = Trie(suf_link=-1)
words = dict()
for _ in range(m):
    word = input()
    words[word] = 'No'
    trie.add_string(word)
bfs(trie)
state = trie
for char in text:
    if state == trie and char not in state.move:
        state.move[char] = trie
    elif char in state.move:
        state = state.move[char]
    elif state != trie and char not in state.move:
        v = state.suf_link
        while v != -1:
            if char in v.move:
                state.move[char] = v.move[char]
                state = v.move[char]
                break
            v = v.suf_link
        if v == -1:
            state.move[char] = trie
            state = trie
    if state.word in words:
        words[state.word] = 'Yes'
    v = state.suf_link
    while v != -1:
        if v.word in words:
            words[v.word] = 'Yes'
        v = v.suf_link
for word in words:
    print(words[word])
