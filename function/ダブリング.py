def pow(m,n):
    ans = 1
    while n>0:
        if bin(n&1)==bin(1):
            ans *=m
        m*=m
        n = n>>1
    return ans