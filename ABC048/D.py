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
S = input()
n = len(S)
if n%2:
    if S[0]==S[-1]:
        print('Second')
    else:
        print('First')
else:
    if S[0]==S[-1]:
        print('First')
    else:
        print('Second')