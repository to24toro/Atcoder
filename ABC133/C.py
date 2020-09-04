mod = 2019
l,r= map(int,input().split())
if r-l+1>=2019:
    print(0);exit()
ans = 2020
for i in range(l,r+1):
    for j in range(i+1,r+1):
        ans = min(ans, i*j%mod)
print(ans)

