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
<<<<<<< HEAD
=======
h,w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]
for i in range(h):
    for ii in range(i+1,h):
        for j in range(w):
            for jj in range(j+1,w):
                if A[i][j]+A[ii][jj]>A[i][jj]+A[ii][j]:
                    print('No');exit()
print('Yes')
>>>>>>> c0748bd4c077c3dfd6e4d18e63f762403879af12
