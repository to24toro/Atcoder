N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
import bisect
As = [0]
for i in range(N):
    As.append(As[-1]+A[i])
Bs = [0]
for i in range(M):
    Bs.append(Bs[-1]+B[i])
ans = 0
for i in range(len(As)):
    v = K-As[i]
    if v ==0: ans = max(ans,i)
    elif v >0:
        idx = bisect.bisect_right(Bs,v)
        if idx==0: ans = max(ans,i)
        else: ans = max(ans,i+idx-1)
print(ans)
