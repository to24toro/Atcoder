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
    dic[P[i]]= i+1
L = [0,0,dic[n],n+1,n+1]
for i in range(n-1,0,-1):
    j = bisect_right(L,dic[i])
    a,b,c,d = L[j-2],L[j-1],L[j],L[j+1]
    ans += ((d-c)*(dic[i]-b)+(b-a)*(c-dic[i]))*i
    insort_right(L,dic[i])
print(ans)
