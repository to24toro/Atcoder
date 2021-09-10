from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n = int(input())
C=list(map(int,input().split()))
C.sort()
ans = 0
mod = 10**9+7
for i in range(1,n+1):
    ans += C[i-1]*(n-i+2)
    ans%=mod
print(ans*pow(2,2*n-2,mod)%mod)