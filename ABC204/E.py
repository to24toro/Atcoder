from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m = map(int,input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    a,b,c,d = map(int,input().split())
    a-=1
    b-=1
    g[a].append(())