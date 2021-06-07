from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

S = input()
T = input()
dic = defaultdict(list)
for i,s in enumerate(S):
    dic[s].append(i)
pre = -1
cnt = 0
for i,t in enumerate(T):
    l = dic[t]
    if len(l)==0:
        print(-1);exit()
    idx = bisect_right(l,pre)
    if idx==len(l):
        cnt += 1
        pre = l[0]
    else:
        pre = l[idx]

print(cnt*len(S)+pre+1)