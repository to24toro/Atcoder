n,d = map(int,input().split())
X = list(map(int,input().split()))
from bisect import bisect_left,bisect_right
ans = 0
for i,x in enumerate(X):
    l = bisect_left(X, x-d)
    r = bisect_right(X, x+d)
    ans += (i-l)*(r-i-1)
    m = bisect_right(X, x+d)
    m = max(0,m-i-1)
    ans-=m*(m-1)//2
print(ans)
#9 min