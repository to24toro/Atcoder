n,t = map(int,input().split())
A = list(map(int,input().split()))
X = A[:n//2]
Y = A[n//2:]
x = len(X)
y = len(Y)
def helper(X,x,t):
    res = []
    for bit in range(1<<x):
        tmp = 0
        for i in range(x):
            if (bit>>i)&1:
                tmp+=X[i]
        if tmp<=t:
            res.append(tmp)
    return res
L = helper(X,x,t)
R = helper(Y,y,t)
L.sort()
R.sort()
ans = 0
from bisect import bisect_right
for l in L:
    tmp = 0
    T = t-l
    if T>=0 and l<=t:
        idx = bisect_right(R,T)
        if idx==0:
            tmp = l
        elif idx==len(R):
            tmp=l+R[-1]
        else:
            tmp = l+R[idx-1]
        ans =max(ans,tmp)
print(ans)
