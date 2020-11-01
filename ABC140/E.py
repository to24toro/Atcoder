n = int(input())
P = list(map(int,input().split()))
dic = {}
for i,p in enumerate(P):
    dic[p] = i+1
L = [0,0,dic[n],n+1,n+1]
ans=0
from bisect import bisect_left,insort_left
for p in range(n-1,0,-1):
    x = bisect_left(L,dic[p])
    ans+=(L[x+1]-L[x])*(dic[p]-L[x-1])*p
    ans+=(L[x-1]-L[x-2])*(L[x]-dic[p])*p
    insort_left(L,dic[p])
print(ans)