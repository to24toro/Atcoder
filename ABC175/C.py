x,k,d = map(int,input().split())
v = abs(abs(x)//d)
w = abs(x)%d
if v >=k:
    print(abs(abs(x)-k*d))
else:
    k-=v
    if k%2:
        print(abs(w-d))
    else:
        print(w)