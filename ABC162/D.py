n = int(input())
s = input()
r,g,b = [0]*(n+1),[0]*(n+1),[0]*(n+1)
for i in range(1,n+1):
    if s[i-1]=='R':
        r[i] =r[i-1]+1
        g[i] = g[i-1]
        b[i] = b[i-1]
    elif s[i-1] =='G':
        r[i] =r[i-1]
        g[i] = g[i-1]+1
        b[i] = b[i-1]
    else:
        r[i] =r[i-1]
        g[i] = g[i-1]
        b[i] = b[i-1]+1
ans = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        p = ['R','G','B']
        if s[i-1] ==s[j-1]:
            continue
        else:
            p.remove(s[i-1])
            p.remove(s[j-1])
            if 2*j-i-1 <n and p[0] ==s[2*j-i-1]:
                ans -=1
            if p[0]=='R':
                ans += r[-1]-r[j]
            elif p[0]=='B':
                ans += b[-1]-b[j]
            else:
                ans += g[-1]-g[j]
print(ans)
            