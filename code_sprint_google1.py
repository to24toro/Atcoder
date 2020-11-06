t = int(input())
import math
from copy import deepcopy
from collections import deque
def helper(l,idx):
    l[A[idx]]=idx
    for i in range(1,len(l)):
        if l[i]>0 and math.gcd(A[idx],i)==1:
            return l[i],l
    return -1,l
for _ in range(t):
    n = int(input())
    A = [0]+list(map(int,input().split()))
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    l = [0]*(101)
    q = deque([(1,l)])
    ans = [0]*(n+1)
    while q:
        x,l_c = q.popleft()
        s,t = helper(l_c,x)
        ans[x]=s
        l_d = deepcopy(t)
        for y in g[x]:
            q.append((y,l_d))
    print(ans[1:])