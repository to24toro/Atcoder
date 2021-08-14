from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
S = input()
q = int(input())
K = list(map(int,input().split()))
D = []
M = []
C = []
for k in K:
    ans = 0
    d,m,c,dm = 0,0,0,0
    for i,s in enumerate(S):
        if i-k>=0:
            if S[i-k]=="D":
                d-=1
                dm-=m
            elif S[i-k]=="M":
                m-=1
        if S[i] =='D':
            d += 1
        elif S[i]=='M':
            m += 1
            dm += d
        elif S[i] =="C":
            c += 1
            ans += dm
    print(ans)


