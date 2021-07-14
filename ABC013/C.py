from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,h = map(int,input().split())
a,b,c,d,e = (map(int,input().split()))
ans = INF
for noeat in range(n+1):
    need=max(0,noeat*e-h-d*(n-noeat)+1)
    gotoeat=(need-1)//(b-d)+1
    if gotoeat<=n-noeat:
        ans=min(ans,c*(n-noeat)+(a-c)*gotoeat)
print(ans)