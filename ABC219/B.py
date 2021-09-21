from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
a = input()
b = input()
c = input()
S = [a,b,c]
T = input()
ans = []
for t in T:
    if t=='1':
        ans.append(S[0])
    elif t =='2':
        ans.append(S[1])
    else:
        ans.append(S[2])
print(''.join(ans))