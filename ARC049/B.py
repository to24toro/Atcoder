n = int(input())
X,Y,C = [],[],[]
for _ in range(n):
    x,y,c = map(int,input().split())
    X.append(x)
    Y.append(y)
    C.append(c)
l,r = 0,10**9

def chk(x):
    for i in range(n):
        for j in range(i+1,n):
            dx = abs(X[i]-X[j])
            dy = abs(Y[i]-Y[j])
            if dx>(x/C[i]+x/C[j]) or dy>(x/C[i]+x/C[j]): return False
    return True
for i in range(50):
    mid = (l+r)/2
    if chk(mid):
        r = mid
    else:
        l = mid
print(r)
