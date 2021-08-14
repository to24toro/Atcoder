from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0
for a,b in zip(A,B):
    cnt += abs(a-b)
if cnt<=k and abs(cnt-k)%2==0:
    print('Yes')
else:
    print('No')



