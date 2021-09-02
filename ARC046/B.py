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
A,B = map(int,input().split())
if n<=A:
    print('Takahashi');exit()
if A==B:
    a = A+1
    if n%a==0:
        print('Aoki')
    else:
        print('Takahashi')
else:
    if A>B:
        print('Takahashi')
    else:
        print('Aoki')