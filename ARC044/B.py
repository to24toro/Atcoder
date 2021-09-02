from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n = int(input())
A = list(map(int,input().split()))
dic = defaultdict(int)
if A[0]!=0:
    print(0);exit()
for a in A:
    dic[a]+=1
if dic[0]>1:
    print(0);exit()
ans = 1
mod = 10**9+7
L = sorted(dic.items())
mx = L[-1][0]
P = [1,1]
for i in range(1,n):
    P.append(P[-1]*i%mod)
for i in range(1,mx+1):
    if dic[i]:
        # ans *= dic[i]
        ans *= pow(2,dic[i]*(dic[i]-1)//2,mod)
        ans *=pow(pow(2,dic[i-1],mod)-1,dic[i],mod)
        ans %= mod
    else:
        print(0);exit()
# print(ans)
print(ans%mod)