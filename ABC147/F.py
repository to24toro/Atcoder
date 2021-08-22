from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,x,d = map(int,input().split())
def helper(k):
    l = ((i*x)//d+k*(k-1)//2)
    r = ((i*x)//d+k*(2*n-k-1)//2)
    return (l,r)
if d==0:
    if x==0:
        print(1)
    else:
        print(n+1)
    exit()

dic = defaultdict(list)
for i in range(n+1):
    dic[(i*x)%abs(d)].append(helper(i))
ans = 0
def solve(i):
    L = dic[i]
    L.sort()
    res = L[0][1]-L[0][0]+1
    pre = L[0][1]
    for l,r in L[1:]:
        if l>pre:
            res += r-l+1
            pre = r
        else:
            if r<=pre:
                continue
            else:
                res += r-pre
                pre = r
    return res


for key,li in dic.items():
    ans +=solve(key)
print(ans)