N,K = map(int,input().split())
A = list(map(int,input().split()))
# A.sort()
P = []
M = []
z = 0
for a in A:
    if a==0:z += 1
    elif a>0:P.append(a)
    else: M.append(a)
P.sort()
M.sort()
def helper(n):
    if n < 0:
        res = 0
        p = 0
        for m in range(len(M)):
            while p < len(P) and P[p]*M[m] > n:
                p += 1
            res += len(P)-p
    elif n ==0:
        res = len(P)*len(M) + z*(N-z) + z*(z-1)//2
    else:
        res = len(P)*len(M) + z*(N-z) + z*(z-1)//2
        pr = len(P)-1
        for pl in range(len(P)):
            while pr > pl and P[pl]*P[pr] > n:
                pr-=1
            res += max(0,pr-pl)
        ml = 0
        for mr in range(len(M)-1,-1,-1):
            while mr >ml and M[ml]*M[mr] > n:
                ml += 1
            res += max(0,mr-ml)
    return res

l = -10**18
r = 10**18
while True:
    num = (l+r)//2
    if helper(num) < K:
        l = num
    else:
        r = num
    if r-l <=1:
        print(r)
        break
