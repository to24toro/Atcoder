from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
dic = {}
def helper(x,y,z):
    if (x,y,z) in dic:
        return dic[(x,y,z)]
    if x==100 or y==100 or z==100:
        dic[(x,y,z)]=0
        return 0
    dic[(x,y,z)] =  (x*(helper(x+1,y,z)+1)+y*(helper(x,y+1,z)+1)+z*(helper(x,y,z+1)+1))/(x+y+z)
    return dic[(x,y,z)]
x,y,z = map(int,input().split())
print(helper(x,y,z))