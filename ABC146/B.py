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
S = input()
T = ""
for s in S:
    T += chr((ord(s)-ord('A')+n)%26+ord('A'))
print(T)