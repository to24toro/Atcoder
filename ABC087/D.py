from collections import deque
N,M = map(int,input().split())
graph = [[] for i in range(N)]
for _ in range(M):
  l,r,d = map(int,input().split())
  graph[l-1].append((r-1,d))
  graph[r-1].append((l-1,-d))

q = deque([i for i in range(N)])
pos = [None for i in range(N)]
while q:
  x = q.popleft()
  if pos[x] == None:
    pos[x] = 0
  for y,d in graph[x]:
    if pos[y] == None:
      pos[y] = pos[x] + d
      q.appendleft(y)
      continue
    if pos[y] != pos[x] + d:
      print("No")
      exit()

print("Yes")
