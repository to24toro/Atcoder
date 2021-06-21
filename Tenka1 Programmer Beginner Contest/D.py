from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,k = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for a,b in L:
    if k|a==k:ans += b
for i in range(30):
    if k>>i&1==0:continue
    m = k-(1<<i)|(1<<i)-1
    tmp = 0
    for a,b in L:
        if m|a==m:tmp+=b
    ans = max(ans,tmp)
print(ans)
