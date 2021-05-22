n = int(input())
A = list(map(int,input().split()))
mod = 998244353
ans = 0
A.sort()
for a in A:
    ans += a**2
    ans%=mod

if n==1:
    print(ans);exit()
mn = A[0]
for a in A[1:]:
    ans += a*mn
    mn *=2
    mn+=a
    ans%=mod
    mn%=mod
    # print(ans)

print(ans)