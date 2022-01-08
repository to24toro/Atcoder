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

l,r = map(int,input().split())
S = list(input())
S[l-1:r] = S[l-1:r][::-1]
print(''.join(S))