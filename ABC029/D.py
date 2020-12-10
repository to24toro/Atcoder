s = input()
n = int(s)
ans = 0
for k in range(len(s),0,-1):
    d1 = 10**(k-1)
    d10 = d1*10
    d,m = divmod(n+1,d10)
    ans += d1*d+min(d1,max(0,m-d1))

print(ans)
