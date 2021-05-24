from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

S = input()
ans = []
S = S[::-1]
for s in S:
    if s=='0':
        ans.append('0')
    elif s=='1':
        ans.append('1')
    elif s=='6':
        ans.append('9')
    elif s=='8':
        ans.append('8')
    else:
        ans.append('6')

print(''.join(ans))