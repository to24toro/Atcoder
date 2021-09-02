n = int(input())
L = []
for _ in range(n):
    x,y,c = map(int,input().split())
    L.append((x,y,c))

l,r = 0,10**10

while r-l>1e-7:
    m = (r+l)/2
    llx = -10**10
    rrx = 10**10
    lly = -10**10
    rry = 10**10
    for x,y,c in L:
        tmp = m/c
        llx = max(llx,x-tmp)
        rrx = min(rrx,x+tmp)
        lly = max(lly,y-tmp)
        rry = min(rry,y+tmp)
    if llx<=rrx and lly<=rry:
        r = m
    else:
        l = m
print(r)

