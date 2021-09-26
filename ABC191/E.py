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
def ext_gcd(a,b):
    if b==0:
        return (1,0,a)
    x,y,g = ext_gcd(b,a%b)
    return (y,x-(a//b)*y,g)
def inv_gcd(a,b):
    x,y,g = ext_gcd(a,b)
    return (g,x%b)
# returns (x % lcm(M), lcm(M)),  (x = R[i] (mod M[i]))
def crt(R,M):
    N = len(R)
    r0 = 0
    m0 = 1
    for i in range(N):
        r1 = R[i]%M[i]
        m1 = M[i]
        if m0<m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0%m1 !=r1:
                return (0,0)
            continue
        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g != 0:
            return (0, 0) # x nai
        x = ((((r1 - r0) // g) % u1) * im) % u1
        r0 += x * m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return (r0, m0)
t = int(input())
for _ in range(t):
    x,y,p,q = map(int,input().split())
    ans = INF
    for r1 in range(x,x+y):
        for r2 in range(p,p+q):
            t,lcm = crt([r1,r2],[(x+y)*2,p+q])
            if lcm == 0:continue
            ans = min(ans,t)
    print('infinity' if ans ==INF else ans)

