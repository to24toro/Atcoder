n = int(input())
A = list(map(int,input().split()))
p = A[:n]
q = A[n:2*n]
qr = []
for i in q:
    qr.append(-i) 
r = A[2*n:]
import heapq
heapq.heapify(p)
heapq.heapify(qr)
while qr:
    pval = heapq.heappop(p)
    qrval = heapq.heappop(qr)
    if pval < -qrval:
        heapq.heappush(p,qrval)
    else:
        heapq.heappush(p,pval)
        break

