x,k,d = map(int,input().split())
x = abs(x)
if k*d<=x:
    print(x-k*d)
    exit()
k-=x//d
x-=x//d*d
if k%2==0:
    print(x)
else:
    print(d-x)