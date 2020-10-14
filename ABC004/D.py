R,G,B = map(int,input().split())

def calc(n):
    return n*(n+1)//2

ans = float('inf')
for l in range(-150,G+151):
    r = G-l-1
    if r>=0 and l>=0:
        a = calc(l) + calc(r)
    elif r<0:
        a = calc(l)-calc(r)
    else:
        a = calc(r)-calc(l)
    if l>=100:
        a += calc(R+l-100)-calc(l-100)
    else:
        rs = 99-l
        if rs<(R-1)//2:
            a += calc(rs)+calc(R-rs-1)
        else:
            rr = (R-1)//2
            a += calc(rr) + calc(R-rr-1)
    if r>=100:
        a += calc(B+r-100)-calc(r-100)
    else:
        ls = 99-r
        if ls<(B-1)//2:
            a += calc(ls)+calc(B-ls-1)
        else:
            ll = (B-1)//2
            a += calc(ll) + calc(B-ll-1)
    ans =min(a,ans)
print(ans)