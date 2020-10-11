n,x,y = map(int,input().split())
A = list(map(str,input().split()))
B = list(map(str,input().split()))
b_B = B.count('B')
r_B = B.count('R')
from copy import deepcopy
res = float('inf')
for i in range(2<<n):
    tmp = deepcopy(A)
    ans = 0
    for j in range(n):
        if (i>>j)&1:
            if tmp[j]=='B':
                tmp[j] = 'R'
            else:
                tmp[j] = 'B'
    b_tmp = tmp.count('B')
    r_tmp = tmp.count('R')
    if b_tmp!=b_B or r_tmp != r_B:
        continue
    else:
        ans += y*int(bin(i).count('1'))
        s,t = 0,0
        while s<n:
            if tmp[s]!=B[s]:
                for k in range(s,n):
                    if B[s]==tmp[k]:
                        t = k
                        break
                while k>s:
                    tmp[k],tmp[k-1] = tmp[k-1],tmp[k]
                    k-=1
                ans += x*(t-s)
            s += 1
    res = min(res,ans)
print(res)



