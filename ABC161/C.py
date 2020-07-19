n,k = map(int,input().split())
v = n//k
ans = float('inf')
for i in (1,-1):
    for j in (1,-1):
        for l in (v,v+1):
            ans = min(ans,abs(i*n+j*l*k))
print(ans)