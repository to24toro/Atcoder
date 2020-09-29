n,Q = map(int,input().split())

h = n
w = n
H = [n for _ in range(n)]
W = [n for _ in range(n)]
ans = pow(n-2,2)
for _ in range(Q):
    a,x = map(int,input().split())
    if a==1:
        if x<w:
            for i in range(x+1,w):
                H[i] = h
            w = x
            ans-=h-2
        else:
            ans-=H[x]-2
    else:
        if x<h:
            for i in range(x+1,h):
                W[i] = w
            h = x
            ans-=w-2
        else:
            ans-=W[x]-2
print(ans)

