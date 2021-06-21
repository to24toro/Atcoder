from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.adj = [[] for _ in range(N + 1)]
        self.lv = None
        self.progress = None
        self.inf = 1 << 60

    def add_edge(self, fr, to, cap):
        # [to, cap, rev]
        forward = [to, cap, None]
        backward = forward[2] = [fr, 0, forward]
        self.adj[fr].append(forward)
        self.adj[to].append(backward)

    def bfs(self, s, t):
        que = deque([s])
        lv = [-1] * (self.N + 1)
        lv[s] = 0
        while que:
            v = que.popleft()
            lvv = lv[v]
            for u, cap, _ in self.adj[v]:
                if cap and lv[u] == -1:
                    que.append(u)
                    lv[u] = lvv + 1
                    if u == t:
                        break
        self.lv = lv

    def dfs(self, s, t, flow):
        st = deque([s])
        st_f = deque([flow])
        while st:
            v = st[-1]
            f = st_f[-1]
            if v == t:
                for i in range(len(st) - 1, 0, -1):
                    p = st[i - 1]
                    edge = self.adj[p][self.progress[p] - 1]
                    edge[1] -= f
                    edge[2][1] += f
                return f
            if self.progress[v] == len(self.adj[v]):
                st.pop()
                st_f.pop()
                continue
            else:
                adj_v = self.adj[v]
                for i in range(self.progress[v], len(adj_v)):
                    i = self.progress[v]
                    self.progress[v] = i + 1
                    u, cap, rev = adj_v[i]
                    if not cap or self.lv[u] != self.lv[v] + 1:
                        continue
                    else:
                        st.append(u)
                        st_f.append(min(st_f[-1], cap))
                        break

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s, t)
            if self.lv[t] < 0:
                return flow
            self.progress = [0] * (self.N + 1)
            flow_new = self.dfs(s, t, self.inf)
            while flow_new:
                flow += flow_new
                flow_new = self.dfs(s, t, self.inf)


