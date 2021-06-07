from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,m = map(int,input().split())
X = list(map(int,input().split()))

s = defaultdict(int)
d = defaultdict(int)
cnt = Counter(X)
ans = 0
for x in X:
    if cnt[x]>1:
        d[x%m]+=1
    else:
        s[x%m]+=1
for i in range(m):
    if i==0:
        tmp =s[i]+d[i]
        ans += tmp*(tmp-1)//2
    else:
        mn = min(s[i],s[m-i])
        s[i]-=mn
        s[m-i]-=mn
        ans += mn
        if s[i]>0:
            mn2 = min(s[i],d[m-i])
            ans+=mn2
            s[i]-=mn2
            d[m-i]-=mn2
            mn3 = min(d[i],d[m-i])
            ans += mn3
            d[m-i]-=mn3
            d[i]-=mn3
            ans +=d[i]*()

