n,q = map(int,input().split())
L = []
A = [0]*(n+1)
for _ in range(q):
    l,r = map(int,input().split())
    A[l-1]+=1
    A[r]-=1
from itertools import accumulate
A = list(accumulate(A))
ans = ''
for a in A:
    ans+='0' if a%2==0 else '1'
print(ans[:-1])