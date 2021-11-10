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
def lcm(x,y):
    	return x//math.gcd(x,y)*y
def choose(n,r):
	return math.factorial(n)//math.factorial(r)//math.factorial(n-r)
def choose2(n,r,k):
	ans=1
	for i in range(k):
		ans*=choose(n-r*i,r)
	return ans//math.factorial(k)

def dfs(rest,L,n,cnt):
    if n == 1:
        return cnt*pow(L,K,MOD)%MOD
    else:
        ans = dfs(rest,L,n-1,cnt)
        for i in range(1,rest//n+1):
            ans += dfs(rest-i*n,lcm(L,n),n-1,cnt*choose2(rest,n,i)*math.factorial(n-1)**i%MOD)
        return ans%MOD
N,K = map(int,input().split())
MOD=998244353
print(dfs(N,1,N,1)%MOD)

# 未確定の要素がrest個あって、現時点でのLCMがLで、長さnumより大きな巡回置換の個数は確定済みで、そんな順列がcnt個ある