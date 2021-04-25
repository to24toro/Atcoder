n = int(input())
S = input()
L = [s for s in S]
Q = int(input())
f = 1
for i in range(Q):
    t,a,b = map(int,input().split())
    a-=1
    b-=1
    if t==1:
        if f==0:
            a = (a+n)%(2*n)
            b = (b+n)%(2*n)
        L[a],L[b] = L[b],L[a]
    else:
        f = 1-f

if f == 0:
    ans = L[n:]+L[:n]
else:
    ans = L
print(''.join(ans))