from itertools import accumulate


n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
S = [0]*(m+1)
sum = 0
for l,r,s in L:
    l-=1
    S[l]+=s
    S[r]-=s
    sum += s
SS = list(accumulate(S))
mn = min(SS[:-1])
if mn==0:
    print(sum)
else:
    print(sum-mn)