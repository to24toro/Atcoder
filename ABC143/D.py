n = int(input())
L = list(map(int,input().split()))
L.sort()
import bisect
ans = 0
for i in range(1,n):
    for j in range(i+1,n):
        tmp = L[:i]
        v = L[j]-L[i]
        idv = bisect.bisect_right(tmp,v)
        if idv!=len(tmp):
            ans += len(tmp)-idv
print(ans)

