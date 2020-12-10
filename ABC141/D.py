n,m = map(int,input().split())
A = list(map(lambda x : -int(x),input().split()))
import heapq
hq = []
heapq.heapify(A)
for _ in range(m):
    a = heapq.heappop(A)
    a=-(abs(a)//2)
    heapq.heappush(A,a)
print(-sum(A))