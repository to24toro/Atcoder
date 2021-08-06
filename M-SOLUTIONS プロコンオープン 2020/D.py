from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
C = list(map(int,input().split()))
C.sort()
q = deque([0])
s = [-1]*n
s[0] = C.pop()
ans = 0
while q:
    x = q.popleft()
    for y in g[x]:
        if s[y]<0:
            s[y] = C.pop()
            ans += s[y]
            q.append(y)

print(ans)
print(*s)