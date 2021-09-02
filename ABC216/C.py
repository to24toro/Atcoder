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
if n==1:
    print('A');exit()
ans = ""
for i in range(119):
    if n%2:
        ans+="A"
        n-=1
    else:
        ans +='B'
        n//=2
    if n==1:
        ans +="A"
        print(ans[::-1])
        exit()
