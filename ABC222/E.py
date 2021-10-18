from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,m,k = map(int,input().split())
K = k
A = list(map(lambda x:int(x)-1,input().split()))
D = defaultdict(int)
g = [[] for _ in range(n)]
for i in range(n-1):
    u,v = map(int,input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)
for i in range(m-1):
    a,b = A[i],A[i+1]
    if b<a:
        a,b = b,a
    q = deque([(a,[a])])
    s = [0]*n
    s[a]+=1
    f =False
    while q and not f:
        x,li = q.popleft()
        if x==b:
            for j in range(len(li)-1):
                c,d = li[j],li[j+1]
                if c>d:c,d = d,c
                D[(c,d)] += 1
            f = True
        for y in g[x]:
            if s[y]==0:
                s[y] = 1
                q.append((y,li+[y]))


X = []
MOD = 998244353

for k,v in D.items():
    X.append(v)
X.sort()

lx = len(X)
s = sum(X)
dp = [[0]*(s+1) for _ in range(lx+1)]
dp[0][0] = 1
for i in range(1,lx+1):
    x =X[i-1]
    for j in range(s+1):
        dp[i][j] = dp[i-1][j]
        if j-x>=0:
            dp[i][j] += dp[i-1][j-x]
        dp[i][j]%=MOD
L = dp[-1]
ans = 0
for i,l in enumerate(L):
    b = i
    r = s-b
    if r-b==K and r>=0 and b>=0:
        ans += l
print(ans%MOD)
# for b in range(lx):
#     r = lx-b
#     dp = [[0]*(b+1) for _ in range(lx)]
