from collections import deque

def solve(L):
    h = len(L)
    w = len(L[0])
    dist = [(1,0),(-1,0),(0,1),(0,-1)]
    res = 0
    for i in range(h):
        for j in range(w):
            if L[i][j] =='x':
                res += 1
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()
                    for dx,dy in dist:
                        X = x + dx
                        Y = y + dy
                        if 0<=X<h and 0<=Y<w and L[X][Y] =='x':
                            L[X][Y] = '0'
                            q.append((X,Y))
    return res
h = int(input())
L = [list(input()) for _ in range(h)]
print(solve(L))