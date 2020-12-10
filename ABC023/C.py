from collections import Counter
R,C,K = map(int,input().split())
n = int(input())
H = [0]*R
W = [0]*C
p = set()
for _ in range(n):
    r,c = map(int,input().split())
    r-=1
    c-=1
    H[r]+=1
    W[c]+=1
    p.add((r,c))
ch=Counter(H)
cw = Counter(W)
ans = 0
for k,v in ch.items():
    if k<=K:
        ans += v*cw[K-k]
for r,c in p:
    if H[r]+W[c]==K:
        ans-=1
    if H[r]+W[c]==K+1:
        ans +=1
print(ans)

