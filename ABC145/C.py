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
L = list(range(n))
S = [list(map(int,input().split())) for _ in range(n)]
N = math.factorial(n)
ans = 0
for l in permutations(L):
    ll = list(l)
    for i in range(n-1):
        ans += math.sqrt((S[ll[i]][0]-S[ll[i+1]][0])**2+(S[ll[i]][1]-S[ll[i+1]][1])**2)
print(ans/N)
    
