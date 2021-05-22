n,x = map(int,input().split())
L = [int(input()) for _ in range(n)]
A = L[:n//2]
B = L[n//2:]
a = []
b = []
from collections import defaultdict
def helper(A):
    N = len(A)
    dic = defaultdict(int)
    for bit in range(1<<N):
        tmp = 0
        for j in range(N):
            if (bit>>j)&1:
                tmp+=A[j]
        dic[tmp] += 1
    return dic
da = helper(A)
db = helper(B)
ans = 0
for k,v in da.items():
    if k==x:
        ans += v
    else:
        ans +=v*db[x-k]
# ans += db[x]
print(ans)