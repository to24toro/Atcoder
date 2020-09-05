from collections import deque
n, m = map(int, input().split())
w = [set() for _ in range(n + 1)]
for _ in range(m):
  u, v = map(int, input().split())
  w[u].add(v)
s, t = map(int, input().split())

memo = [[-1,-1,-1] for _ in range(n+1)]

d = deque()
d.append((s,0,0))
while d:
    i,q,r = d.popleft()
    for nx in w[i]:
        if nx ==t and r ==2:
            print((q+1)//3)
            exit()
        if memo[nx][(r+1)%3] == -1:
            memo[nx][(r+1)%3] = q+1
            d.append((nx,q+1,(r+1)%3))
print(-1)