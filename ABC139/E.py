n = int(input())
L = []
for _ in range(n):
    a = list(map(lambda x:int(x)-1,input().split()))
    L.append(a)
cnt = [0]*n
from collections import deque
q = deque(i for i in range(n))
cur = [0]*n
while q:
    p = q.popleft()
    if cnt[p]==n-1:
        continue
    r = L[p][cnt[p]]
    if cnt[r]==n-1:
        continue
    if p==L[r][cnt[r]]:#試合がおこなわれる
        cnt[p]+=1
        cnt[r]+=1
        now = max(cur[p],cur[r])+1
        cur[p]=now
        cur[r]=now
        q.append(p)
        q.append(r)
if min(cnt)<n-1:
    print(-1);exit()
print(max(cur))


