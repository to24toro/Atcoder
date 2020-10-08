n,X = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i,a in enumerate(A):
    if (X>>i)&1:
        ans += a
print(ans)