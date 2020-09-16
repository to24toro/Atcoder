mod = 10**9+7
n =int(input())
A = list(map(int,input().split()))
tmp = []
for i in range(n):
    tmp.append(abs(n-2*i-1))
A.sort()
tmp.sort()
for a,t in zip(A,tmp):
    if a!=t:
        print(0);exit()
from collections import Counter
from math import factorial
ans = 1
cnt_a = Counter(A)
for k,v in cnt_a.items():
    ans *= factorial(v)
    ans %=mod
print(ans)