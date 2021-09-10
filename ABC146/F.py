#####segfunc#####
def segfunc(x, y):
    return min(x, y)
    # return max(x, y)
    # return x^y
#################

##### 単位元 #####
ide_ele = float("inf")

#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

N, M = map(int, input().split())
S = input()

dp = [ide_ele] * (N+1)
dp[N] = 0

sg = SegTree(dp, segfunc, ide_ele)

for i in range(N-1, -1, -1):
    if S[i] == "1":
        continue
    nxt = sg.query(i, min(i+M+1, N+1))
    if nxt == ide_ele:
        print(-1)
        exit()
    dp[i] = nxt + 1
    sg.update(i, dp[i])

now = 0
last = 0
ans = []
cu = dp[0]
flag = True
while flag:
    for j in range(last+1, last+1+M):
        if S[j] == "0" and dp[j] == cu-1:
            last = j
            if j == N:
                flag = False
                break
            break
    ans.append(last-now)
    cu = dp[last]
    now = last

print(" ".join(map(str, ans)))

