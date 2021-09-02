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
for i in range(3):
    if S[i]==S[i+1]:
        print('Bad');exit()
print('Good')