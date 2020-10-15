n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    s = 1/n
    cur = i
    while cur<k:
        cur *= 2
        s*=0.5
    ans += s
print(ans)