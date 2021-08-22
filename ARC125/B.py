from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
N = int(input())
if N==1:
    print(1);exit()
N2 = N**2
m = math.sqrt(N**2-N)
ans = int(math.sqrt(N))
mod = 998244353
def helper(x):
    return (N+x)*(N-x+1)//2
print(ans)
f = False
for p in range(1,int(m)+1):
    l = math.sqrt(1+p**2)
    r = int(math.sqrt(N+p**2))
    print(l,r)
    if r==N:
        q = p
        f=True
        break
    ans += int(r-l)+1
    ans%=mod
# ans*=2
ans%=mod
if f:
    ans += (N+1-q)*(N+2-q)//2
    ans%=mod

    

print(ans)

