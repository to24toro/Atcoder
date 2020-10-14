N, M = map(int, input().split())
mod = 10 ** 9 + 7
Query = [int(input()) for _ in range(N)]
T = [1]*(M+1)
A = [-1,0]
dp = [1]
last = 1
for i,q in enumerate(Query,2):
    last = max(T[q],last)
    a = A[-1]-A[last-1]
    a%=mod
    dp.append(a)
    A.append(A[-1]+a)
    T[q] = i
print(dp[-1]%mod)