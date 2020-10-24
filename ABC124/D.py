n,k = map(int,input().split())
S = input()
A = [0]
if S[0]=='0':
    A.append(0)
cnt = 1
for s1,s2 in zip(S,S[1:]):
    if s1!=s2:
        A.append(cnt)
        cnt = 1
    else:
        cnt += 1
A.append(cnt)
from itertools import accumulate
A = list(accumulate(A))
n = len(A)
ans = 0
for s in range(1,n,2):
    t = min(n-1,s+2*k)
    ans = max(ans,A[t]-A[s-1])
print(ans)