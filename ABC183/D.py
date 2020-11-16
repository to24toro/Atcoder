n,w = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
A = [0]*(2*10**5+2)
for s,t,p in L:
    A[s]+=p
    A[t]-=p
from itertools import accumulate
P = list(accumulate(A))
# print(P[:20])
for p in P:
    if p>w:
        print('No');exit()
print('Yes')