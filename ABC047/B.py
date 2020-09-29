w,h,n = map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(n)]
l = 0
r = w
d = 0
u  =h
for x,y,a in A:
    if a==1:
        l = max(x,l)
    elif a ==2:
        r = min(r,x)
    elif a ==3:
        d = max(y,d)
    else:
        u = min(y,u)
if u-d<0 or r-l<0:
    print(0)
else:
    print((u-d)*(r-l))