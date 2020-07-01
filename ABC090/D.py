ans = 0
N,K = map(int,input().split())
if K==0: print(N*N);exit()
for i in range(K+1,N+1):
    v = N//i
    ans += v*(i-K) + max(0,N%i-K+1)
print(ans)