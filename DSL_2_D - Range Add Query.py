class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None or i==j:
            return self.el[i]
        return self.sum(j) - self.sum(i)
n,q = map(int,input().split())
ans = []
bt = BIT(n)
for q in range(q):
    t, *cmd = map(int, input().split())
    if t:
        print(bt.get(cmd[0]))
    else:
        s, t, x = cmd
        bt.add(s, x)
        if t < n:
            bt.add(t+1, -x)
        