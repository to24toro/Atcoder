# k-bit目のxorを考えた時a+bはmod 2^(k+1)で考えると高々2^(k+1)*2未満
#k-bit目が1の範囲は[2^k,2*2^k)と[3*2^k,4*2^k)
n = int(input())
a=list(map(int,input().split()))
b_=list(map(int,input().split()))
ans=0
from bisect import bisect_left as bl
def helper(l,r,b):
    return bl(b,r)-bl(b,l)

for i in range(29):
    T = pow(2,i)
    tmp = 0
    b=sorted([x%(2*T) for x in b_])
    for ai in a:
        ai%=2*T
        tmp += helper(T-ai,2*T-ai,b)
        tmp += helper(3*T-ai,4*T-ai,b)
    ans += T*(tmp%2)
print(ans)