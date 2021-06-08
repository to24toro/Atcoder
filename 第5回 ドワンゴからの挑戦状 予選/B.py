from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,k = map(int,input().split())
A = list(map(int,input().split()))
arr = []
for i in range(n):
    for j in range(i,n):
        if j>i:
            arr.append(arr[-1]+A[j])
        else:
            arr.append(A[j])
x = 0

cnt = [1]*(len(arr))
# print(arr)
for i in range(40,-1,-1):
    c = 0
    for j in range(len(arr)):
        if cnt[j] and (arr[j]>>i)&1:
            c+=1
    if c>=k:
        x+=1<<i
        for j in range(len(arr)):
            if not (arr[j]>>i)&1:
                cnt[j]=0
print(x)