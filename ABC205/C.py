from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

a,b,c = map(int,input().split())
A = abs(a)
B = abs(b)
if c%2:
    if a<0:
        if b<0:
            if a<b:
                print('<')
            elif a==b:
                print('=')
            else:
                print('>')
        else:
            print('<')
    else:
        if b<0:
            print('>')
        else:
            if a<b:
                print('<')
            elif a==b:
                print('=')
            else:
                print('>')
else:
    if A==B:
        print('=')
    elif A<B:
        print('<')
    else:
        print('>')