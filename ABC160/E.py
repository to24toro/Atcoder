import heapq
x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort()
apples = p[:x] + q[:y]
heapq.heapify(apples)
while r:
    val = r.pop()
    apple = heapq.heappop(apples)
    if apple>= val:
        heapq.heappush(apples,apple)
        break
    else:
        heapq.heappush(apples,val)
print(sum(apples))