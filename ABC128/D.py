n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
s = sum(A)
for l in range(k+1):
    for r in range(k+1):
        if l+r>k or n-r<l:
            continue
        tmp = A[:l] + A[n-r:]
        tmp.sort()
        val = sum(tmp)
        for i in range(min(k-l-r,len(tmp))):
            if tmp[i]<0:
                val-=tmp[i]
            else:
                break
        ans = max(ans,val)
print(ans)