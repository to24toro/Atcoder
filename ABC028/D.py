n,k = map(int,input().split())
ans = 0
ans += (k-1)*(n-k)*6/(n**3)
ans += (k-1)*3/(n**3)
ans += (n-k)*3/(n**3)
ans += 1/(n**3)
print(ans)