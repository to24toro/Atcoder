from itertools import combinations
n = int(input())
C = [int(input()) for _ in range(n)]

frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]//frac[n-r]//finv[r]
D = [0]*n
for i in range(n):
    c = C[i]
    for j in range(n):
        if c%C[j]==0:
            D[i]+=1
ans = 0
for i in range(n):
    d = D[i]
    if d%2:
        ans += (d+1)//2/d
    else:
        ans += 0.5
print(ans)