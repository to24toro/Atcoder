import collections
H,W,K = map(int,input().split())
s1,e1,s2,e2 = map(int,input().split())
s1-=1
e1-=1
s2-=1
e2-=1
L = []
board = []
for _ in range(H):
    a = input()
    L.append(a)
for i in range(H):
    l = L[i]
    tmp = []
    for j in range(len(l)):
        tmp.append(l[j])
    board.append(tmp)

queue = collections.deque()
queue.append([0,s1,e1])
seen = [[float('inf')]*(W) for _ in range(H)]
destination = [(1,0),(-1,0),(0,1),(0,-1)]
while queue:
    cost,x,y = queue.popleft()
    seen[x][y] = cost
    if x==s2 and y ==e2:
        print(cost);exit()
        break
    for dx,dy in destination:
        X,Y = x,y
        for i in range(1,K+1):
            NX = X +i*dx
            NY = Y + i*dy
            if 0>NX or NX>=H or 0>NY or NY>=W or seen[NX][NY] < seen[X][Y]+1: break
            else:
                if board[NX][NY]=='@':
                    break
                elif seen[NX][NY] ==float('inf'):
                    queue.append([cost+1,NX,NY])
                    seen[NX][NY] = cost+1

print(-1)