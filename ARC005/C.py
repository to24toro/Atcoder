from heapq import heappop, heappush
import sys
input = sys.stdin.readline
H,W = map(int,input().split())

C = ['-' * (W+2)]
C += ['-' + input().rstrip() + '-' for _ in range(H)]
C.append('-' * (W+2))

for i,row in enumerate(C):
  j = row.find('s')
  if j != -1:
    sx,sy = i,j
  j = row.find('g')
  if j != -1:
    gx,gy = i,j

INF = 3
dist = [[INF] * (W+2) for _ in range(H+2)]
dist[sx][sy] = 0
q = [(0,sx,sy)]

while q:
  d,x,y = heappop(q)
  if d > dist[x][y]:
    continue
  dist[x][y] = d
  for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
    x1 = x + dx
    y1 = y + dy
    c = C[x1][y1]
    if c == '-':
      continue
    if c == '#':
      d1 = d + 1
    else:
      d1 = d
    if dist[x1][y1] <= d1:
      continue
    dist[x1][y1] = d1
    heappush(q, (d1,x1,y1))

answer = 'YES' if dist[gx][gy] <= 2 else 'NO'
print(answer)