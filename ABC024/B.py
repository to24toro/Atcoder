n,t = map(int,input().split())
s = 0
ans = 0
for i in range(n):
    a = int(input())
    if i==0:
        s = a
    else:
        if s+t<a:
            ans += t
        else:
            ans += a-s
        s = a
print(ans+t)
