from itertools import *
from collections import *
from heapq import *
from random import randint
import math
import sys
sys.setrecursionlimit(1<<20)

n,m,k = map(int,input().split())
P = set()
for _ in range(m):
    a,b = map(int,input().split())
    P.add((a,b))
    P.add((b,a))

rep = 250000
cnt = 0

for _ in range(rep):
    S = list(range(n))
    for _ in range(k):
        a = randint(0,n-1)
        b = (randint(1,n-1) + a)%n
        S[a],S[b] = S[b],S[a]
    for i in range(n):
        if (S[i-1],S[i]) in P:
            cnt += 1
            break
print((rep-cnt)/rep)