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
n,k = map(int,input().split())
A = list(map(int,input().split()))
S = [0]
T = [0]+list(accumulate(A))
ans = 0
for a in A:
    S.append(S[-1]+max(a,0))
for i in range(n-k+1):
    res = S[i]+S[-1]-S[i+k]
    res2 =res+T[i+k]-T[i]
    print(res,res2,i)
    ans =max(ans,res,res2)
print(ans)