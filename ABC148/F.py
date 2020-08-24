n,u,v = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
seen = [False]*n
import collections
dic = collections.defaultdict(int)

q = collections.deque([])
q.append((u,0,[u],False))
tmp =[]
while q:
    s,cnt,li,f = q.popleft()
    seen[s] = True
    dic[s] = cnt
    for e in g[s]:
        if not seen[e]:
            if f:
                tmp.append(e)
            if e ==v:
                tmp += li+[e]
                f = True
            q.append((e,cnt+1,li+[e],f))
set_ = set(tmp)
ans = 0
for i in range(n):
    if i not in set_:
        ans = max(ans,dic[i])
val = dic[v]-dic[u]
if val<=ans:
    if val%2==0:
        print(ans + val-1)
    else:
        print(ans + val-1)
else:
    if val%2==0:
        print(ans+val-1)
    else:
        print(ans + val-1)        
