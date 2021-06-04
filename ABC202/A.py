from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
A = list(map(int,input().split()))
print(21-sum(A))