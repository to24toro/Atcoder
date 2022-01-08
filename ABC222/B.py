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

n,p = map(int,input().split())
A =list(map(int,input().split()))
ans = 0
for a in A:
    if a<p:ans+=1
print(ans)
