ans = 0
n = int(input())
A = list(map(int,input().split()))
from itertools import accumulate
S = list(accumulate(A))
T = [A[0]]
for i in range(1,n):
    T.append(T[-1]^A[i])
for l in range(n):
    ok = l
    ng = n
    while ng -ok>1:
        m = (ng+ok)//2
        t = T[m]
        if l:
            t^=T[l-1]
        s = S[m]
        if l:
            s-=S[l-1]
        if s==t:
            ok=m
        else:
            ng = m
    ans += ok-l+1
    # print(ans)
print(ans)