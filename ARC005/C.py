from heapq import heappop, heappush
import sys
input = sys.stdin.readline
H,W = map(int,input().split())
C = [list(input()) for _ in range(H)]

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
  if d>dist[x][y]:
    continue
  for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
    X = x + dx
    Y = y + dy
    if 0<=X<H and 0<=Y<W:
      c = C[X][Y]
      if c == "#":
        d1 = d+1
      else:
        d1 = d
			if d1>=dist[X][Y]:
    		continue
			dist[X][Y] = d1
			heappush(q,(d1,X,Y))

answer = 'YES' if dist[gx][gy] <= 2 else 'NO'
print(answer)