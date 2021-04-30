w,h = map(int,input().split())
P = [int(input()) for _ in range(w)]
Q = [int(input()) for _ in range(h)]
R = []
for i,p in enumerate(P):
    R.append((p,0))
for j,q in enumerate(Q):
    R.append((q,1))
R.sort()
ans = 0
for cost,c in R:
    if c:
        ans += cost*(w+1)
        h-=1
    else:
        ans += cost*(h+1)
        w-=1
print(ans)