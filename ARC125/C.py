from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,k = map(int,input().split())
A = list(map(int,input().split()))
cnt=1
if k==1:
    L = [i for i in range(1,n+1)]
    print(*L[::-1]);exit()
else:
    set_ = set(A)
    ans = []
    B = []
    for i,a in enumerate(A):
        if a==i+1:
            ans.append(a)
        else:
            B.append(a)
    X = []
    for i in range(1,n+1):
        if i not in set_:
            X.append(i)
    X.reverse()
    
    for i in range(len(B)):
        if i<len(B)-1:
            if B[i]==len(ans)+1:
                ans.append(B[i])
            else:
                ans.append(B[i])
                if X:
                    ans.append(X.pop())
        else:
            if X:
                for x in X:
                    if x>B[i]:
                        ans.append(x)
                ans.append(B[i])
                for x in X:
                    if x<B[i]:
                        ans.append(x)
            else:
                ans.append(B[i])
    if not B:
        b = ans.pop()
        ans += X
        ans.append(b)
    print(*ans)

