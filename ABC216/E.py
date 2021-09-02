from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,k = map(int,input().split())
A = list(map(int,input().split()))

l,r = 0,10**10

while r-l>1:
    m = (r+l)//2
    cnt = 0
    for a in A:
        cnt += max(a-m,0)
    if cnt>k:
        l = m
    else:
        r = m
def helper(j,i):
    return j*(j+1)//2-i*(i+1)//2
ans = 0
A.sort(reverse=True)
for a in A:
    if a>r:
        ans += helper(a,r)
        k-=a-r
if k<=0:
    print(ans);exit()
p = r*min(k,n)

print(ans + p)