from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import numpy as np
from functools import lru_cache
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]