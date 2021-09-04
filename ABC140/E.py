from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
ans = 0
P = list(map(int,input().split()))
dic = {}
for i in range(n):
    dic[P[i]]= i
L = [-1,-1,dic[n],n,n]

for i in range(n-1,0,-1):
    j = bisect_right(L,dic[i])
    a,b,c,d = L[j-2],L[j-1],L[j],L[j+1]
    ans += i*((d-c)*(dic[i]-b) + (b-a)*(c-dic[i]))
    insort_right(L,dic[i])
print(ans)