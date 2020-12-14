m,n = map(int,input().split())
def pow_doubling(m,n,mod):
    ans = 1
    while n>0:
        if bin(n&1)==bin(1):
            ans *=m
            ans %=mod
        m*=m
        m %=mod
        n = n>>1
    return ans
print(pow_doubling(m,n,10**9+7))