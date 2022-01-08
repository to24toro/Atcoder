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
n = int(input())
A = [0]*n
for _ in range(n-1):
    a,b =map(int,input().split())
    a-=1
    b-=1
    A[a]+=1
    A[b]+=1
for i in range(n):
    if A[i]==n-1:
        print('Yes')
        exit()
print('No')
>>>>>>> c0748bd4c077c3dfd6e4d18e63f762403879af12
