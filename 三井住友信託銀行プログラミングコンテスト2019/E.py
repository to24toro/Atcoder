n = int(input())
mod = 10**9+7
ans = 1
cnt = 0
c = [0,0,0]
A = list(map(int,input().split()))
for i,a in enumerate(A):
    if a not in c:
        print(0);exit()
    else:
        cnt = c.count(a)
        ans *= cnt
        ans %= mod
        idx = c.index(a)
        c[idx]+=1
print(ans%mod)
    