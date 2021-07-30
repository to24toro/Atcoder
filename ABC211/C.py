from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
S = input()
MOD = 10**9+7
T = 'chokudai'
dic = defaultdict(list)
for i,s in enumerate(S):
    tmp = ord(s)-ord('a')
    dic[tmp].append(i)
ans = 0
p = len(dic[ord('i')-ord('a')])
def dfs(x,i):
    global ans
    i += 1
    if i ==8:
        ans += p-bisect_left(dic[ord('i')-ord('a')],x)
        return
    t = T[i]
    l = dic[ord(t)-ord('a')]
    idy = bisect_left(l,x)
    if idy==len(l):
        return
    for j,y in enumerate(l[idy:]):
        # print(t,idy,y)
        dfs(y,i)

for i,x in enumerate(dic[ord('c')-ord('a')]):
    dfs(x,0)
print(ans)