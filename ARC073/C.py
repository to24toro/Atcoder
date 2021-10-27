from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,w = map(int,input().split())
dic = defaultdict(list)
for i in range(n):
    a,b = map(int,input().split())
    if i==0:
        s = a
    dic[a].append(b)
dic[s].sort(reverse=True)
dic[s+1].sort(reverse=True)
dic[s+2].sort(reverse=True)
dic[s+3].sort(reverse=True)
A = dic[s]
B = dic[s+1]
C = dic[s+2]
D = dic[s+3]
SA = [0]+list(accumulate(A))
SB = [0]+list(accumulate(B))
SC = [0]+list(accumulate(C))
SD = [0]+list(accumulate(D))
ans = -float('inf')
for i in range(len(SA)):
    for j in range(len(SB)):
        for k in range(len(SC)):
            for l in range(len(SD)):
                p = i*s+j*(s+1)+k*(s+2)+l*(s+3)
                if p>w:continue
                res = SA[i]+SB[j]+SC[k]+SD[l]
                ans = max(ans,res)
print(ans)