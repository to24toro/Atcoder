
d = [0]
n = int(input())
C = input()
A = []
for c in C:
    if c=='B':
        A.append(0)
    elif c=='W':
        A.append(1)
    else:
        A.append(2)
for i in range(1,n+1):
    cnt = 0
    while i%3==0:
        cnt += 1
        i//=3
    d.append(d[-1]+cnt)
# print(d)
mod = 3
frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    k = i+1
    while k%3==0:
        k//=3
    frac[i+1] = (k)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+1):
    k = n-i+1
    while k%3==0:
        k//=3
    finv[n-i] = finv[n-i+1]*k%mod
ans = [1]
for i in range(1,n):
    if d[n-1]!=d[n-i-1]+d[i]:
        ans.append(0)
    else:
        res = frac[n-1]*finv[n-1-i]*finv[i]
        res%=mod
        ans.append(res)
a = 0
for i in range(n):
    a+=A[i]*ans[i]
a*=pow(-1,n-1)
a%=mod
if a==0:
    print('B')
elif a==1:
    print('W')
else:
    print('R')