import collections
import heapq
N,Q = map(int,input().split())
dic = collections.defaultdict(list)
check = collections.defaultdict(int)
mem = collections.defaultdict(int)
for i in range(N):
    a,b = map(int,input().split())
    heapq.heappush(dic[b],[-a,i+1])
    check[i+1] = a
    mem[i+1] = b
L = []
for _ in range(Q):
    c,d = map(int,input().split())
    L.append([c,d])
for c,d in L:
    ans = float('inf')
    heapq.heappush(dic[d],[-check[c],c])
    mem[c] = d
    for key in dic.keys():
        if dic[key] and mem[dic[key][0][1]] != key:
            heapq.heappop(dic[key])
        if len(dic[key])>0:
            ans = min(-dic[key][0][0],ans)
    print(ans)
