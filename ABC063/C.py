# N,M= map(int,input().split())
# N,M = max(N,M),min(N,M)
# mod = 10**9+7

# n = 100010
# frac = [1]*(n+1)
# for i in range(n):
#     frac[i+1] = (i+1)*frac[i]%mod
# if N==M+1:
#     print(frac[N]*frac[M]%mod)
# elif N==M:
#     print(frac[N]*frac[M]*2%mod)
# else:
#     print(0)

n = int(input())
C = [int(input()) for _ in range(n)]
sum = sum(C)
C.sort()
if sum%10:print(sum)
else:
    for c in C:
        if (sum-c)%10:
            print(sum-c)
            exit()
    print(0)
