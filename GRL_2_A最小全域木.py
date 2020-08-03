v,e = map(int,input().split())
edges = [[] for _ in range(v)]
for _ in range(e):
    s,t,w = map(int,input().split())
    edges[s-1].append((w,t-1))
    edges[t-1].append((w,s-1))
set_ = set()
import heapq
hq = edges[0]
heapq.heapify(hq)
set_.add(0)
cnt = 0
while len(set_)<v:
    w,t = heapq.heappop(hq)
    if t in set_: continue
    set_.add(t)
    cnt += w
    for w,s in edges[t]:
        heapq.heappush(hq,(w,s))
print(cnt)
    