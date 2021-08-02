from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
X = input()
X = [int(i) for i in X]
s = set()
for x in X:
    s.add(x)
if len(s)==1:
    print('Weak')
else:
    for i in range(3):
        if X[i]==9:
            if X[i+1]==0:
                print('Weak');exit()
        else:
            if X[i]+1==X[i+1]:
                print('Weak');exit()
    print('Strong')