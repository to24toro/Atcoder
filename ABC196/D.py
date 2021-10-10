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

h,w,a,b = map(int,input().split())

ans = 0
def dfs(i,bit,a,b):
    if i==h*w:
        global ans
        ans += 1
        return
    if bit >>i&1:
        dfs(i+1,bit,a,b)
        return
    if b:
        dfs(i+1,bit | 1<<i,a,b-1)
    if a:
        if i%w!=w-1 and not bit&1<<(i+1):
            dfs(i+1,bit|1<<i|1<<(i+1),a-1,b)
        if i+w<h*w:
            dfs(i+1,bit|1<<i|1<<(i+w),a-1,b)
dfs(0,0,a,b)
print(ans)