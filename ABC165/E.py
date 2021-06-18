from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,m = map(int,input().split())
# if n%2==0:
#     nn = n//2
#     for i in range(1,nn+1):
#         x = i
#         y = n+1-i
#         print(x,y)
#         if i==m:
#             exit()
# else:
nn = n//2
for i in range(1,m+1):
    x = i
    y = n+1-i
    print(x,y)
    if i==m:
        exit()
