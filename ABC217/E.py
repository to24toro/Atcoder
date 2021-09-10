import heapq
from sys import exit
from collections import defaultdict,deque
q = int(input())
L = deque([])
hq = []
ans = []
cur = float('inf')
for i in range(q):
    query = list(map(int,input().split()))
    if query[0]==1:
        L.append(query[1])
    elif query[0]==2:
        if not hq:
            p = L.popleft()
        else:
            p = heapq.heappop(hq)
        ans.append(p)
    else:
        while L:
            heapq.heappush(hq,L.popleft())
for a in ans:
    print(a)
