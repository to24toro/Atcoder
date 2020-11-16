a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))
e,f = list(map(int,input().split()))
ans = 0
for i in range(a,b+1):
    if i<c:
        x = d-c+1
    else:
        if d<=i:
            x=0
        else:
            x = d-i
    if i<e:
        x*=f-e+1
    else:
        if f<=i:
            x = 0
        else:
            x*=f-i
    ans += x
print(ans/((b-a+1)*(d-c+1)*(f-e+1)))