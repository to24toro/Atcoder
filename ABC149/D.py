n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()
ans = []
a,b,c = 0,0,0
for i in range(n):
    if i>=k:
        if t[i]==ans[i-k]:
            ans.append('X')
            continue
    if t[i] =='r':
        ans.append('r')
        c += 1
    elif t[i]=='s':
        ans.append('s')
        a += 1
    else:
        ans.append('p')
        b += 1
print(a*r+b*s+c*p)