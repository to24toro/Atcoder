n = int(input())
S = list(map(int,input().split()))
ans = 0
for c in range(1,n):
    score = 0
    set_ = set()
    for x in range(n):
        if n-1-(x+1)*c<=0:
            break
        if x*c in set_:
            break
        if n-1-x*c in set_:
            break
        if x*c==n-1-x*c:
            break
        a = n-1-x*c
        set_.add(x*c)
        set_.add(a)
        score += S[a]
        score += S[x*c]
        ans = max(ans,score)

print(ans)