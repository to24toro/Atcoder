t = int(input())
P = []
for _ in range(t):
    n,a,b = map(int,input().split())
    P.append((n,a,b))
mod = 10**9+7

for n,a,b in P:
    if n -a -b <0:
        print(0)
    else:
        x = (n-a+1)*(n-b+1)-(n-a-b+2)*(n-a-b+1)
        x *= x
        ans =((n-a+1)*(n-a+1)* (n-b+1)*(n-b+1))
        ans -= x
        print(ans%mod)

