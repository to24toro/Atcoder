
from collections import deque
N = int(input())
Y = {}
for _ in range(N):
    c,d = map(int,input().split())
    Y[c] = d  
X = []
for _ in range(N):
    a,b = map(int,input().split())
    X.append([a,b])

X.sort()
dq = deque(X)
cnt =0
while dq:
    x,y = dq.popleft()
    sorted_Y = sorted(Y.items(),reverse=True, key = lambda x:x[1])
    for key,val in sorted_Y:
        if key <x and val<y:
            cnt += 1
            del Y[key]
            break
    
print(cnt)
