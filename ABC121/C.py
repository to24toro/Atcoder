import collections
N,M = map(int,input().split())
l=[]
for _ in range(N):
    a,b = map(int,input().split())
    l.append((a,b))
l.sort()
L = collections.deque(l)
ans = 0
while M>0:
    a,b = L.popleft()
    if M>=b:
        ans += a*b
    else:
        ans +=a*M
    M-=b
print(ans)