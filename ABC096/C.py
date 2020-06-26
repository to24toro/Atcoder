H,W = map(int,input().split())
A = []
for _ in range(H):
    a = input()
    a.split()
    A.append(a)
dist = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(H):
    for j in range(W):
        if A[i][j]=='#':
            cnt =0
            for dx,dy in dist:
                if 0<=i+dx<H and 0<=j+dy<W:
                    if A[i+dx][j+dy]=='#':
                        cnt +=1
            if cnt ==0: print('No');exit()
print('Yes')
