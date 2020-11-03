n,a,b = map(int,input().split())
X = list(map(int,input().split()))
ans = 0
for i in range(1,n):
    if (X[i]-X[i-1])*a<b:
        ans += (X[i]-X[i-1])*a
    else:
        ans += b
print(ans)