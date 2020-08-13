n,m = map(int,input().split())
P = [0]
for _ in range(n):
    P.append(int(input()))
P.sort()
Q = []
for p1 in P:
    for p2 in P:
        Q.append(p1+p2)
import bisect
Q.sort()
ans = 0
for q in Q:
    val = m-q
    idx = bisect.bisect_right(Q,val)
    if idx==0:continue
    ans = max(ans,Q[idx-1] + q)
print(ans)