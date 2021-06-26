class Trie:

    def __init__(self, R: int = 26, code=int, decode=str):
        self.R = R
        self.edges = [[-1]*self.R]
        self.is_end = [0]
        self.parents = [-1]
        self.size = [0]
        self.node_label = [-1]
        self.code=code
        self.decode=decode

    def add(self, S: str):
        code, decode = self.code, self.decode
        edges, R, parents, is_end, size, node_label = self.edges, self.R, self.parents, self.is_end, self.size, self.node_label
        p = 0
        for s in S:
            s = code(s)
            if edges[p][s] == -1:
                edges[p][s] = len(edges)
                edges.append([-1]*R)
                parents.append(p)
                is_end.append(0)
                size.append(0)
                node_label.append(s)
            size[p] += 1
            p = edges[p][s]
        is_end[p] += 1
        size[p] += 1

    def find(self, S: str, prefix: bool = True):
        code, decode = self.code, self.decode
        edges, R, parents, is_end = self.edges, self.R, self.parents, self.is_end
        p = 0
        for s in S:
            s = code(s)
            if edges[p][s] == -1:
                return False
            p = edges[p][s]
        return prefix or is_end[p] > 0

    def bisect_left(self, S: str):
        """ Sが辞書に存在する場合は rank 関数"""
        code, decode = self.code, self.decode
        edges, R, parents, is_end, size = self.edges, self.R, self.parents, self.is_end, self.size
        p = 0
        res = 0
        for s in S:
            s = code(s)
            if edges[p][s] == -1:
                for q in edges[p][:s]:
                    if q == -1:
                        continue
                    res += size[q]
                res += is_end[p]
                return res
            for q in edges[p][:s]:
                if q == -1:
                    continue
                res += size[q]
            res += is_end[p]
            p = edges[p][s]

        return res

    def bisect_right(self, S: str):
        code, decode = self.code, self.decode
        edges, R, parents, is_end, size = self.edges, self.R, self.parents, self.is_end, self.size
        p = 0
        res = 0
        for s in S:
            s = code(s)
            if edges[p][s] == -1:
                for q in edges[p][:s]:
                    if q == -1:
                        continue
                    res += size[q]
                res += is_end[p]
                return res
            for q in edges[p][:s]:
                if q == -1:
                    continue
                res += size[q]
            res += is_end[p]
            p = edges[p][s]

        return res+1

    def delete(self, S: str):
        code, decode = self.code, self.decode
        edges, R, parents, is_end, size, parents, node_label = self.edges, self.R, self.parents, self.is_end, self.size, self.parents, self.node_label
        p = 0
        for s in S:
            s = code(s)
            if edges[p][s] == -1:
                return False
            p = edges[p][s]
        if is_end[p] > 0:
            is_end[p] -= 1
            while p != -1:
                size[p] -= 1
                if size[p] == 0:
                    edges[parents[p]][node_label[p]] = -1
                p = parents[p]

    def minimum(self, k: int = 0):
        code, decode = self.code, self.decode
        edges, size, is_end = self.edges, self.size, self.is_end
        p = 0
        res = []
        k += 1
        while k > 0:
            k -= is_end[p]
            if k <= 0:
                return res
            for s, q in enumerate(edges[p]):
                if q == -1:
                    continue
                if size[q] >= k:
                    p = q
                    res.append(decode(s))
                    break
                else:
                    k -= size[q]
        return res

    def maximum(self, k: int = 0):
        return self.minimum(len(self)-1-k)

    def count(self):
        """ 登録済み単語数 """
        return len(self)

    def __len__(self):
        return self.size[0]

    def __iter__(self):
        code, decode = self.code, self.decode
        edges, R, is_end, base, parents, node_label = self.edges, self.R, self.is_end, self.code, self.parents, self.node_label

        next_set = [(0, [])]
        while next_set:
            p, S = next_set.pop()
            if is_end[p]:
                for _ in range(is_end[p]):
                    yield S
            for s, q in list(enumerate(edges[p]))[::-1]:
                if q == -1:
                    continue
                T = S+[decode(s)]
                next_set.append((q, T))

    def __str__(self):
        return "\n".join("".join(s) for s in self)

    def __getitem__(self, i):
        if i < 0:
            i = len(self)-1+i
        return self.minimum(i)

    def draw(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        from networkx.drawing.nx_pydot import graphviz_layout

        G = nx.DiGraph()
        labels = {}
        for p, edge in enumerate(self.edges):
            for s, q in enumerate(edge):
                if q == -1:
                    continue
                G.add_node(q)
                labels[q] = self.decode(s)
                # labels[q]=(self.decode(s),self.size[q])
                G.add_edge(p, q)

        pos = graphviz_layout(G, prog="dot")
        nx.draw(G, pos=pos, with_labels=True, labels=labels, node_size=1000)
        plt.axis("off")
        plt.show()

N = int(input())
Ss = [[ord(c) - ord('a') for c in input()] for _ in range(N)]

trie = Trie(code=lambda t: t, decode=lambda t: t)

ret = 0
Ss.sort(key=lambda s: len(s))
print(Ss)
for S in Ss:
    cnter = [0] * 26
    for c in S:
        cnter[c] += 1
    v = 0
    for c in reversed(S):
        for alpha in range(26):
            if cnter[alpha]:
                word_end = trie.edges[v][alpha]
                if word_end != -1 and trie.is_end[word_end] > 0:
                    ret += 1
        cnter[c] -= 1
        nv = trie.edges[v][c]
        print(S,v,nv)
        if nv == -1:
            break
        v = nv

    trie.add(S[::-1])

print(ret)
