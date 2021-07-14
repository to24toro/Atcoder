from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
n = int(input())
W = list(map(int,input().split()))
mod = 998244353
dp = [[[0]*(10001) for _ in range(n)]]
