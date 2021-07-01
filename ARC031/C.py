from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
            
n = int(input())
A = list(map(int,input().split()))
bit = Bit(n)
L,R = [0]*n,[0]*n
for i in range(1,n):
    bit.add(A[i-1],1)
    L[i] = bit.sum(n)-bit.sum(A[i]-1)
B = A[::-1]
bit = Bit(n)

for i in range(1,n):
    bit.add(B[i-1],1)
    R[i] = bit.sum(n)-bit.sum(B[i]-1)
R = R[::-1]
ans = 0
for i in range(n):
    ans += min(L[i],R[i])
print(ans)