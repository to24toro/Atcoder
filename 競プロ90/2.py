from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import sys
sys.setrecursionlimit(1<<20)
ANS = []
n = int(input())
if n%2:
    print();exit()
for bit in range(1<<n):
    A = []
    cur = 0
    s = 0
    f = True
    ans = ''
    for j in range(n):
        if (1<<j)&bit==0:
            cur-=1
            ans += ')'
        else:
            cur += 1
            s += 1
            ans += '('
        if cur <0:
            f = False
            break
    if s != n//2:
        f = False
    if f:
        ANS.append(ans)
ANS.sort()
print(*ANS,sep = '\n')
