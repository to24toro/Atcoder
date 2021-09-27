from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
k = int(input())
a,b = map(str,input().split())
A=0
a = a[::-1]
b = b[::-1]
for i in range(len(a)):
    A+=pow(k,i)*int(a[i])
B = 0
for i in range(len(b)):
    B+=pow(k,i)*int(b[i])
print(A*B)