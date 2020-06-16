n =int(input())
vw = [(0,0)]  
for _ in range(n):
    vw.append(list(map(int,input().split())))

A  =10
N = min(1<<A,n+1)
memo = [None for _ in range(N)]
L = 10**5+1
memo[0] = [0]*L

for i in range(1,N):
    m = memo[i>>1][:]
    v,w = vw[i]    
    for j in range(L-1,w-1,-1):
        if m[j] < m[j-w]+v:
            m[j] = m[j-w]+v
    memo[i] = m

q = int(input())
ans_ = [0]*q
for _ in range(q):
    u,l = map(int,input().split())
 
    m = u.bit_length() - A
    if m<0: m=0
    dv = [0]*(1<<m)
    dw = [0]*(1<<m)
    for i in range(m):
        v,w = vw[u]
        for j in range(1<<i):
            dv[j+(1<<i)] = dv[j]+v
            dw[j+(1<<i)] = dw[j]+w
        u >>= 1
    
    ans = 0
    for v,w in zip(dv,dw):
        if w <= l:
            val = memo[u][l-w] + v
            if val > ans: ans = val
    ans_[_] = ans
print(*ans_,sep="\n")