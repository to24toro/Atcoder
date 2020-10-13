n,m = map(int,input().split())
W = list(map(int,input().split()))
M = []
min_v = float('inf')
max_w = max(W)
r = 0
W_b = []
T = []
for i in range(m):
    l,v = map(int,input().split())
    if i==0: r = l
    M.append([l,r])
    T.append([v,i])
    min_v = min(min_v,v)
    if r<l:r=l
T.sort()
W_b = []
I = []
for v,i in T:
    W_b.append(v)
    I.append(i)
if max_w>min_v: print(-1);exit()
from itertools import permutations, accumulate
from bisect import bisect_right
ans = float('inf')
cnt = [i for i in range(n)]
for v in permutations(cnt):
    v = list(v)
    W_s = [W[v[0]]]
    res = 0
    for i in range(1,len(v)):
        W_s.append(W_s[-1]+W[v[i]])

    for i,w in enumerate(W_s):
        if i==0: continue
        
        idx = bisect_right(W_b,w)
        # print(idx)
        if idx ==0:
            r = 0
        else:
            q = I[idx-1]
            r = M[q][1]
        res += r

    ans = min(ans,res)
        
print(ans)
    

