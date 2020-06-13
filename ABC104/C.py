import heapq
hq = []
D,G = map(int,input().split())
for i in range(1,D+1):
    p,c = map(int,input().split())
    A = []
    for j in range(1,p+1):
        if j ==p:
            A.append(-100*i-c)
        else:
            A.append(-100*i)
    heapq.heappush(hq,A)
G = -G

ans = 0
count = 0
while ans> G:
    a = heapq.heappop(hq)
    ans += a[0]
    count += 1
    del a[0]
    heapq.heappush(hq,a)
print(count)