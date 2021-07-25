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
B = list(map(int,input().split()))
dic = Counter(B)
ans = set()
for i in range(n):
    b = B[i]
    b1 = b
    dic2 = defaultdict(int)
    dic2[b] += 1
    f =True
    for j in range(1,n):
        b = b^A[j]^A[j-1]
        dic2[b] += 1
    for k,v in dic.items():
        if v!=dic2[k]:
            f = False
            break
    if f:
        a = b1^A[0]
        if a>0:
            ans.add(b1^A[0])
ans = list(ans)
ans.sort()
print(len(ans))
for a in ans:
    print(a)
    
