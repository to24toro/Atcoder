from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,l = map(int,input().split())
a = [i for i in range(2*3**(l-1)+n-1,2*3**(l-1)-1,-1)]
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
b = [Base_10_to_n(x,3) for x in a]
def to1(x):
    res = ""
    for i in x:
        if i=="2":
            res+="1"
        elif i=="1":
            res+="0"
        else:
            res+="2"
    return res
def to0(x):
    res = ""
    for i in x:
        if i=="0":
            res+="1"
        elif i=="2":
            res+="0"
        else:
            res+="2"
    return res
c = [to1(x) for x in b]
d = [to0(x) for x in b]
print(*b,sep='\n')
print(*c,sep='\n')
print(*d,sep='\n')