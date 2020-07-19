from collections import deque
import heapq
k = int(input())
s =[1,2,3,4,5,6,7,8,9,10]
heapq.heapify(s)
li = set()
for val in range(1,2**11):
    v = int(str(bin(val)[2:]))
    li.add(v)
while len(li)<=301000:
    val = heapq.heappop(s)
    li.add(val)
    if str(val)[-1]=='0':
        heapq.heappush(s,10*val)
        heapq.heappush(s,10*val + 1)
    elif str(val)[-1]=='9':
        heapq.heappush(s,10*val + 8)
        heapq.heappush(s,10*val + 9)
    else:
        heapq.heappush(s,10*val + int(str(val)[-1]))
        heapq.heappush(s,10*val + int(str(val)[-1])+1)
        heapq.heappush(s,10*val + int(str(val)[-1])-1)
L = list(li)
L.sort()
print(L[k-1])

