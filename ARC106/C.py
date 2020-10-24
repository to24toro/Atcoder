n,m = map(int,input().split())
d = 10**8
if n==1:
    if m!=0:
        print(-1);exit()
    else:
        print(1, 2);exit()

if abs(m)>m:print(-1);exit()
if m>=0:
    c=1
    print(1,2*(m)+3)
    print(2*(m)+2,2*(m)+4)
else:
    print(-1);exit()
    c = -1
    print(d-2*(m)-3,d-1)
    print(d-2*m-2,d-2*m-4)

for i in range(1,m+1):
    if c>0:
        print(2*i,2*i+1)
    else:
        print(-2*i,-2*i-1)
for j in range(m+2,n):
    if c>0:
        print(2*m+3+2*j,2*m+3+2*j+1)
    else:
        print(d-2*i-2*(m)-3,d-2*i+1-2*(m)-1)
