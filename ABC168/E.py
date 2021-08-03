from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
MOD = 10**9+7
n = int(input())
X = []
for _ in range(n):
    a,b = map(int,input().split())
    X.append((a,b))

def make_pair(A: list):
    import math
    import collections
    dic = collections.defaultdict(int)
    for x,y in A:
        if x==0 and y==0:
            dic[(0,0)] += 1
        elif x==0:
            dic[(0,1)] += 1
        elif y==0:
            dic[(1,0)] += 1
        else:
            x,y = x//math.gcd(x,y),y//math.gcd(x,y)
            if x*y<0:
                x,y = abs(x),-abs(y)
            else:
                x,y = abs(x),abs(y)
            dic[(x,y)] += 1
    return dic

dic = make_pair(X)

ans = 1
s = set()
for a,b in list(dic.keys()):
    if (a,b) in s:continue
    x = dic[(a,b)]
    y = dic[(b,-a)] if b > 0 else dic[(-b,a)]
    s.add((b,-a)) if b > 0 else s.add((-b,a))
    if a != 0 or b != 0:
        ans *= pow(2,x,MOD)+pow(2,y,MOD)-1
    ans %= MOD
ans -= 1
ans %= MOD
ans += dic[(0,0)]
ans %= MOD
print(ans)