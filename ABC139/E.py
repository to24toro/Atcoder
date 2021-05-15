n = int(input())
L = []
for _ in range(n):
    a = list(map(lambda x:int(x)-1,input().split()))
    L.append(a)
from collections import deque
q = deque([i for i in range(n)])
cur_day = [0]*n
cnt = [0]*n
for _ in range(10**6+100000):
    if not q:break
    p = q.popleft()
    day = cur_day[p]
    match = cnt[p]
    pre_match = match
    while match<n-1 and p==L[L[p][match]][cnt[L[p][match]]]:
        day = max(cur_day[p],cur_day[L[p][match]])
        day+=1
        cur_day[p]= day
        cur_day[L[p][match]]=day
        cnt[L[p][match]]+=1
        cnt[p]+=1
        match+=1
        # print(cnt,cur_day,p)
    if match<n-1:
        q.append(p)
# print(cnt,cur_day)
for c in cnt:
    if c!=n-1:
        print(-1);exit()
print(max(cur_day))