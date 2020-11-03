n,k = map(int,input().split())
ans = 0
d = [0]*(2*n+1)
for i in range(2,n+1):
    d[i] =i-1
    d[2*n+2-i] = i-1
d[n+1] = n
for i in range(2,2*n+1):
    if i-k>=2 and i-k<=2*n:
        ans += d[i]*d[i-k]
print(ans)