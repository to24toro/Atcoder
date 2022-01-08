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
s = list(input())
t = list(input())
S = [0]*n
T = [0]*n
for i in range(n):
    if s[i]=='A':
        S[i] = 0
    elif s[i] =="B":
        S[i] = 1
    else:
        S[i] =2
    if t[i]=='A':
        T[i] = 0
    elif t[i] =="B":
        T[i] = 1
    else:
        T[i] =2
P = S[::-1]
Q = T[::-1]
def helper(S,T):
    i = 0
    n = len(S)
    while i<n-2:
        if S[i]==T[i]:
            i += 1
        else:
            if (S[i]==0 and S[i+1]==1 and S[i+2]==2) or (S[i]==1 and S[i+1]==2 and S[i+2]==0) or (S[i]==2 and S[i+1]==0 and S[i+2]==1):
                if S[i]>T[i]:
                    p = (3-(S[i]-T[i]))%3
                else:
                    p = T[i]-S[i]
                S[i] += p
                S[i] %=3
                S[i+1]+=p
                S[i+1]%=3
                S[i+2]+=p
                S[i+2]%=3
            else:
                return 0
            i += 1
        
    for i in range(n):
        if S[i]!=T[i]:
            return 0
    return 1
def helper2(S,T):
    i = 0
    n = len(S)
    while i<n-2:
        if S[i]==T[i]:
            i += 1
        else:
            if (S[i]==0 and S[i+1]==2 and S[i+2]==1) or (S[i]==1 and S[i+1]==0 and S[i+2]==2) or (S[i]==2 and S[i+1]==1 and S[i+2]==0):
                if S[i]>T[i]:
                    p = (3-(S[i]-T[i]))%3
                else:
                    p = T[i]-S[i]
                S[i] += p
                S[i] %=3
                S[i+1]+=p
                S[i+1]%=3
                S[i+2]+=p
                S[i+2]%=3
            else:
                return 0
            i += 1
        
    for i in range(n):
        if S[i]!=T[i]:
            return 0
    return 1
print(S)
f = helper(S,T)
print(S)
e = helper2(P,Q)
if f or e:
    print('YES')
else:
    print('NO')
