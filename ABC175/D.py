n,k = map(int,input().split())
P = list(map(lambda x:int(x)-1,input().split()))
C = list(map(int,input().split()))
ans = -float('inf')
for i in range(n):
    j = i
    s = 0
    cnt = 0
    while True:
        s+=C[j]
        cnt += 1
        j = P[j]
        if j==i:
            break
    score = 0
    j = i
    for l in range(1,cnt+1):
        score += C[j]
        j = P[j]
        if l>k:
            break
        loop = (k-l)//cnt
        x = score + max(s*0,s*loop)
        ans = max(ans,x)
print(ans)