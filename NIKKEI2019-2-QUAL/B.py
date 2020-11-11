n = int(input())
d = list(map(int,input().split()))
if d[0]!=0:print(0);exit()
D = []
for i,x in enumerate(d):
    D.append((x,i))
D.sort()
from collections import Counter
count = Counter(d)
if count[0]>1:print(0);exit()
mod = 998244353
ans = 1
for i in range(1,n):
    ans *= pow(count[i-1],count[i],mod)
print(ans%mod)