from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = list(map(int,input().split()))
AA = [[a,i] for i,a in enumerate(A)]
AA.sort(reverse=True)
B = [0]*(2*n)
for a,i in AA[:n]:
    B[i]=1
q = []
ans = []
l,r = 0,0
cnt = 0
for i in B:
    if not q:
        q.append(["(",i])
        l+=1
    else:
        if l==r:
            q.append(["(",i])
            l+=1
        elif q[-1][1]!=i:
            if q[-1][0]=="(":
                q.append([")",i])
                r += 1
            else:
                q.append(["(",i])
                l += 1
        else:
            if q[-1][0]=="(":
                q.append(["(",i])
                l += 1
            else:
                q.append([")",i])
                r += 1

for s,i in q:
    ans.append(s)
print("".join(ans))