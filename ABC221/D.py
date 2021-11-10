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

n = int(input())
LL = [list(map(int,input().split())) for _ in range(n)]
L = []
for a,b in LL:
    L.append([a,1])
    L.append([a+b,-1])
L.sort()
dic = defaultdict(int)
for x, i in L:
    dic[x]+=i
P = []
for k,v in dic.items():
    if v!=0:
        P.append([k,v])
P.sort()
L = P
# print(L)
cnt = L[0][1]
cur = L[0][0]
D = [0]*(n+1)
for i in range(1,len(L)):
    # print(L[i])
    nx,c = L[i]
    # print("A",nx,cnt,cur)
    D[cnt] += nx-cur
    # print(D)
    cur = nx
    cnt += c
    
print(*D[1:])