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
import heapq
from sys import exit
from collections import defaultdict
class HeapDict:
    def __init__(self,):
        self.h = []
        self.d = defaultdict(set)
    def insert(self,x,i):
        heapq.heappush(self.h,x)
        if i not in self.d:
            self.d[x].add(i)

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,'is not in HeapDict')
            exit()
        else:
            self.d[x]-=1
        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break
    def is_exit(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False
    def get_min(self):
        return self.h[0]



n,q = map(int,input().split())
dic = defaultdict(HeapDict)
for i in range(n):
    a,b = map(int,input().split())
    dic[b].insert((a,i))
infants = []
for k,v in dic.items():
    infants.append(v.get_min())

for _ in range(q):
