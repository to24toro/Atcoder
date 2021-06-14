from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = list(map(int,input().split()))


mx = max(A)
mn = min(A)
if mx-mn>=2:
    print('No');exit()
elif mx-mn==0:
    if mx==n-1:
        print('Yes');exit()
    if 2*mx<=n:
        print('Yes');exit()
    print('No')
else:
    x = A.count(mn)
    y = A.count(mx)
    if x<mx and 2*(mx-x)<=y:
        print('Yes')
    else:
        print('No')