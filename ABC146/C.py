a,b,x = map(int,input().split())
l,r = 0,10**9+1
while l+1 < r:
    i =(l+r)//2
    if a*i + b*len(str(i))<=x:
        l = i
    else:
        r =i
print(l)