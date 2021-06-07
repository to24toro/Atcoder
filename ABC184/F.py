from itertools import *
from collections import *
from heapq import *
from bisect import *
import math

n,t = map(int,input().split())
A = list(map(int,input().split()))
X = A[:n//2]
Y = A[n//2:]
ans = 0
x,y = len(X),len(Y)
XX,YY = [],[]
for bit in range(1<<x):
    tmp = 0
    for i in range(x):
        if (bit>>i)&1:
            tmp += X[i]
    XX.append(tmp)
XX.sort()
for bit in range(1<<y):
    tmp = 0
    for i in range(y):
        if (bit>>i)&1:
            tmp += Y[i]
    YY.append(tmp)
YY.sort()
# print(XX,YY)
for x in XX:
    tmp = t-x
    # print(tmp)
    if tmp==0:
        print(t);exit()
    if tmp<0:
        break
    idx = bisect_right(YY,tmp)
    if idx==0:
        ans = max(ans,x)
    else:
        ans = max(ans,x+YY[idx-1])
    # print(tmp,ans)
print(ans)

