from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
d = [(1,0),(0,1),(0,-1),(-1,0)]
h,w = map(int,input().split())
S = [input() for _ in range(h)]
q = deque([(0,0,0)])
sn = [[INF]*w for _ in range(h)]
while q:
    i,j,c = q.popleft()
    if i<0 or i>=h or j<0 or w<=j:
        continue

    sn[i][j] = c
    if i==h-1 and j==w-1:
        print(c);exit()
    for x in range(4):
        di,dj = d[x]
        I = i + di
        J = j + dj
        if 0<=I<h and 0<=J<w:
            if S[I][J]=='.' and sn[I][J]>c:
                sn[I][J] = c
                q.appendleft((I,J,c))
            elif S[I][J] =='#'and sn[I][J]>c+1:
                sn[I][J] = c + 1
                if x == 0:
                    q.append((I,J,c+1))
                    q.append((I,J+1,c+1))
                    q.append((I,J-1,c+1))
                    q.append((I+1,J-1,c+1))
                    q.append((I+1,J+1,c+1))
                    q.append((I+1,J,c+1))
                elif x==1:
                    q.append((I,J,c+1))
                    q.append((I,J+1,c+1))
                    q.append((I-1,J+1,c+1))
                    q.append((I+1,J,c+1))
                    q.append((I+1,J+1,c+1))
                    q.append((I-1,J,c+1))
                elif x==2:
                    q.append((I,J,c+1))
                    q.append((I-1,J-1,c+1))
                    q.append((I,J-1,c+1))
                    q.append((I+1,J-1,c+1))
                    q.append((I-1,J,c+1))
                    q.append((I+1,J,c+1))
                else:
                    q.append((I,J,c+1))
                    q.append((I-1,J+1,c+1))
                    q.append((I,J-1,c+1))
                    q.append((I-1,J-1,c+1))
                    q.append((I-1,J,c+1))
                    q.append((I,J+1,c+1))
