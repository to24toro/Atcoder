n = int(input())
s = input()
t = input()
sc = s.count('1')
tc = t.count('1')
ans = 0
if sc!=tc:
    print(-1)
else:
    a = 0
    b = 0
    cnt = 0
    for i,j in zip(s,t):
        if i==j and a==0 and b==0:continue
        if i=='0':
            a += 1
        if j=='0':
            b += 1
        if a==b:
            ans += a
            cnt = 0
            a = 0
            b = 0
    print(ans)