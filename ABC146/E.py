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
S = [0] + list(accumulate(A))
dic = defaultdict(int)
ans = 0
T = [(s-i)%k for i,s in enumerate(S)]
sep = min(k,n+1)
for i in range(sep):
    dic[T[i]] += 1
for k,v in dic.items():
    ans += v*(v-1)//2
# print(ans,T)
for j in range(sep,n+1):
    dic[T[j-sep]]-=1
    dic[T[j]]+=1
    ans += dic[T[j]]-1
    # print(j,ans)
print(ans)