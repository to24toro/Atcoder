n,L = map(int,input().split())
k = int(input())
A = list(map(int,input().split()))
def chk(x):
    cnt = 0
    cur = 0
    for i in range(n):
        if A[i]-cur>=x:
            cnt += 1
            cur = A[i]
        else:
            continue
    if l!=A[-1] and L-cur>=x:
        cnt += 1
    return cnt >=(k+1)
l,r = 0,10**9+1
while r-l>1:
    m = (r+l)//2
    if chk(m):
        l = m
    else:
        r = m
    # print(m)
print(l)