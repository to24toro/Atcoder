f = [1]*(101)
for i in range(1,101):
    f[i] = i*f[i-1]
def nCr(n,r):
    return f[n]//f[r]//f[n-r]
n = int(input())
c = [int(input()) for _ in range(n)]
cnt = [0]*n
for i in range(n):
    for j in range(n):
        if i==j:continue
        if c[i]%c[j]==0:
            cnt[i]+=1
ans = 0
for x in cnt:
    for i in range(0,x+1,2):
        ans += nCr(n,x+1)*f[x]*f[n-x-1]
print(ans/f[n])
