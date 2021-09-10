class RollingHash():
    def __init__(self,s,base,mod):
        self.mod = mod
        self.base = base
        self.pw = pw = [1]*(len(s)+1)
        self.length = len(s)
        l = len(s)
        self.h = h = [0]*(l+1)
        v = 0
        for i in range(l):
            h[i+1]=v=(v*base+ord(s[i]))%mod
        v = 1
        for i in range(l):
            pw[i+1]=v=v*base%mod
    def get(self,l,r):#l-rが一致するか
        return (self.h[r]-self.h[l]*self.pw[r-l])%mod
    def check(self,t):
        t_hash = 0
        v= 0
        ans = []
        l = len(t)
        for i in range(l):
            v = v*self.base+ord(t[i])
            t_hash = v%self.mod
            t_hash %=self.mod
            print(t_hash)
        if self.length<l:return ans
        for i in range(self.length-l+1):
            if self.get(i,i+l)==t_hash:
                ans.append(i)
        return ans


# mod = 10**9 + 9; p = 13; q = 19

# p_table = q_table = None
# def prepare(L):
#     global p_table, q_table
#     p_table = [1]*(L+1); q_table = [1]*(L+1)
#     for i in range(L):
#         p_table[i+1] = p_table[i] * p % mod
#         q_table[i+1] = q_table[i] * q % mod

# def rolling_hash(S, W, H):
#     D = [[0]*(W+1) for i in range(H+1)]
#     for i in range(H):
#         su = 0
#         dp = D[i]
#         di = D[i+1]
#         si = S[i]
#         for j in range(W):
#             v = si[j] # v = ord(si[j]) if si[j] is str
#             su = (su*p + v) % mod
#             di[j+1] = (su + dp[j+1]*q) % mod
#     return D
# def get(S, x0, y0, x1, y1):
#     P = p_table[x1 - x0]; Q = q_table[y1 - y0]
#     return (S[y1][x1] - S[y1][x0] * P - S[y0][x1] * Q + S[y0][x0] * (P * Q) % mod) % mod

# # example
# data1 = [
#     [1, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1],
#     [0, 1, 1, 1, 1],
# ]
# data2 = [
#     [1, 0, 1],
#     [1, 0, 1],
# ]
# prepare(L = 5)
# rh1 = rolling_hash(data1, 5, 3)
# rh2 = rolling_hash(data2, 3, 2)
# print(get(rh1, 2, 0, 5, 2) == get(rh2, 0, 0, 3, 2))
# # => "True"

mod = 10**9+7
base=1007
t = input()
p = input()
HT= RollingHash(t,base,mod)
HP = RollingHash(p,base,mod)
l = len(p)
print(HP.h)
pv = HP.get(0,l)
print(HT.check(p))
for i in range(len(t)-len(p)+1):
    if pv ==HT.get(i,i+l):print(i)
