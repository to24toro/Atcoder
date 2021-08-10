from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

h,w,n = map(int,input().split())
s = set()
chk = defaultdict(int)
ANS = [0]*10
dic = defaultdict(lambda:defaultdict(int))
for i in range(n):
    a,b = map(int,input().split())
    s.add((a,b))
    dic[a][b] += 1
# print(dic)
def helper(i,j):
    if i<1 or i>h-2 or j<1 or j>w-2 or chk[(i,j)]:
        return
    ans = 0
    for ii in range(3):
        for jj in range(3):
            ans += dic[i+ii][j+jj]
    if ans>0:
        ANS[ans] += 1

for a,b in s:
    for i in range(3):
        for j in range(3):
            helper(a-i,b-j)
for i in range(1,10):
    ANS[i]//=i
zero = (h-2)*(w-2)-sum(ANS)
for i in range(10):
    if i==0:
        print(zero)
    else:
        print(ANS[i])

