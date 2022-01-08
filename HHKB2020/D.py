from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

T = int(input())
mod = 10**9+7
for _ in range(T):
    n,a,b = map(int,input().split())
    x =0
    ans = (n-a+1)**2*(n-b+1)**2
    if n-a-b>=0:
        x = (n-a-b+2)*(n-a-b+1)//2
    x*=2
    x = (n-a+1)*(n-b+1)-x
    x = x*x
    print((ans-x)%mod)
