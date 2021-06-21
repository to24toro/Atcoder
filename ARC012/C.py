from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

B = [input() for _ in range(19)]
o = 0
x = 0
judge = -1
for i in range(19):
    for j in range(19):
        if B[i][j]=='o':
            o += 1
        elif B[i][j]=='x':
            x += 1
if o-x<0 or o-x>1:
    print('NO')
    exit()
memo = [[-1]*19 for _ in range(19)]
def chk(i,j,s,d,c):
    global judge
    A = [(1,0),(0,1),(1,1)]
    di,dj = A[d]
    I,J = i+di,j+dj
    if c==5:
        if s=='o':
            judge=1
        else:
            judge = 0
        memo[i][j]=1
        if 0<=I<19 and 0<=J<19:
            if B[I][J]==s:
                memo[i][j]=2
                return
    if 0<=I<19 and 0<=J<19:
        if memo[I][J]==-1:
            memo[I][J] = 0
        if B[I][J]==s:
            chk(I,J,s,d,c+1)
    return
for i in range(19):
    for j in range(19):
        if memo[i][j]==2:
            print('NO');exit()
        if memo[i][j]==-1:
            memo[i][j]=0
        if B[i][j]=='o':
            for idx,di,dj in [(0,1,0),(1,0,1),(2,1,1)]:
                I,J = i+di,j+dj
                if 0<=I<19 and 0<=J<19:
                    if B[I][J]=='o':
                        chk(I,J,'o',idx,2)
        elif B[i][j]=='x':
            for idx,di,dj in [(0,1,0),(1,0,1),(2,1,1)]:
                I,J = i+di,j+dj
                if 0<=I<19 and 0<=J<19:
                    if B[I][J]=='x':
                        chk(I,J,'x',idx,2)
if memo.count(1)>1:
    print('NO');exit()
if judge:
    if o<=x:
        print('NO');exit()
else:
    if o>x:
        print('NO');exit()

print('YES')