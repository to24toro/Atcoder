from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
N = int(input())
edges = []
for _ in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    edges.append((a,b))
 

def sumOfDistancesInTree(N, edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
                
    size, up, down = [1] * N, [0] * N, [0] * N

    def post(parent, i): 
        for kid in graph[i]:
            if kid != parent:
                post(i, kid)
                size[i] += size[kid]
                up[i] += up[kid] + size[kid] 
                
    def pre(parent, i):
        if parent!=-1:
            down[i] = down[parent] + (up[parent] - up[i] - size[i]) + (N-size[i])
        for kid in graph[i]:     
            if kid != parent:
                pre(i, kid)
                
    post(-1, 0)            
    pre(-1, 0)            
    return [up[i]+down[i] for i in range(N)] 
ans = sumOfDistancesInTree(N,edges)
print(*ans,sep='\n')