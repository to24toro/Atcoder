from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

S = input()
dic = defaultdict(int)
for s in S:
    dic[s]+=1
for s in S:
    if dic[s]!=2:
        print('No');exit()
print('Yes')