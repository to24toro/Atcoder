mod = 10**9+7
n = int(input())
A = list(map(int,input().split()))
from collections import defaultdict
zero = defaultdict(int)
one = defaultdict(int)
for a in A:
    for i in range(61):
        if a &(1<<i):
            one[i] += 1
        else:
            zero[i] += 1
ans = 0
for i in range(61):
    ans += pow(2,i,mod)*zero[i]*one[i]
    ans %=mod

print(ans%mod)