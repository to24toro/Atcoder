h,w,n,m = map(int,input().split())
g = [[0]*w for _ in range(h)]
cnt = 0
for _ in range(n):
    a,b = map(int,input().split())
    g[a-1][b-1] = 1
    cnt += 1
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1][b-1] = -1

for i in range(h):
    f = False
    for j in range(w):
        if f and g[i][j]==0:
            g[i][j]-=1
            cnt += 1
        if g[i][j]==1:
            f = True
        if g[i][j]==-1:
            f = False
for i in range(h):
    f = False
    for j in range(w-1,-1,-1):
        if f and g[i][j]==0:
            g[i][j]-=1
            cnt += 1
        if g[i][j]==1:
            f = True
        if g[i][j]==-1:
            f = False
for j in range(w):
    f = False
    for i in range(h):
        if f and g[i][j]==0:
            g[i][j]-=1
            cnt += 1
        if g[i][j]==1:
            f = True
        if g[i][j]==-1:
            f = False
for j in range(w):
    f = False
    for i in range(h-1,-1,-1):
        if f and g[i][j]==0:
            g[i][j]-=1
            cnt += 1
        if g[i][j]==1:
            f = True
        if g[i][j]==-1:
            f = False   
# ans = 0   
# for i in range(h):
#     for j in range(w):
#         if g[i][j]>0:
#             ans += 1
print(cnt)
# g = [[(w+1,1)] for _ in range(h+1)]
# f = [[(h+1,1)] for _ in range(w+1)]
# import heapq
# dp = [[0]*(w+1) for _ in range(h+1)]
# for _ in range(n):
#     a,b, = map(int,input().split())
#     heapq.heappush(g[a],(b,0))
#     heapq.heappush(f[b],(a,0))
# for _ in range(m):
#     a,b, = map(int,input().split())
#     heapq.heappush(g[a],(b,1))
#     heapq.heappush(f[b],(a,1))
#     dp[a][b] = -1
# from collections import deque
# # print(g,f)
# ans = 0
# # print(dp)
# for i in range(1,h+1):
#     F = False
#     s,t = 0,0
#     while g[i]:
#         x,cnt = heapq.heappop(g[i])
#         # print(i,x,cnt,F)
#         # print(dp)
#         if cnt ==0:
#             F = True
#         else:
#             t = x
#             if F:
#                 while s<t:
#                     if dp[i][s]!=-1:
#                         dp[i][s] =1
#                     s += 1
#                 F = False
#             s = t
# for i in range(1,w+1):
#     F = False
#     s,t = 0,0
#     while f[i]:
#         x,cnt = heapq.heappop(f[i])
#         if cnt ==0:
#             F = True
#         else:
#             t = x
#             if F:
#                 while s<t:
#                     if dp[s][i]!=-1:
#                         dp[s][i] =1
#                     s += 1
#                 F = False
#             s = t
# ans = 0
# for i in range(1,h+1):
#     for j in range(1,w+1):
#         if dp[i][j] == 1:
#             ans+= 1
# print(ans)

import os
import sys
from io import BytesIO, IOBase
 
 
def main():
    H,W,N,M = map(int,input().split())
    grid = []
    for _ in range(H):
        grid.append([0] * W)
    lightCount = 0
    for _ in range(N):
        a,b = map(int,input().split())
        grid[a-1][b-1] = 1
        lightCount += 1
    for _ in range(M):
        c,d = map(int,input().split())
        grid[c-1][d-1] = 2
    for i in range(H):
        isOn = False
        for j in range(W):
            if isOn and grid[i][j] == 0:
                grid[i][j] = -1
                lightCount += 1
            if grid[i][j] == 1:
                isOn = True
            if grid[i][j] == 2:
                isOn = False
    for i in range(H):
        isOn = False
        for j in range(W-1, -1, -1):
            if isOn and grid[i][j] == 0:
                grid[i][j] = -1
                lightCount += 1
            if grid[i][j] == 1:
                isOn = True
            if grid[i][j] == 2:
                isOn = False
    for j in range(W):
        isOn = False
        for i in range(H):
            if isOn and grid[i][j] == 0:
                grid[i][j] = -1
                lightCount += 1
            if grid[i][j] == 1:
                isOn = True
            if grid[i][j] == 2:
                isOn = False
    for j in range(W):
        isOn = False
        for i in range(H-1, -1, -1):
            if isOn and grid[i][j] == 0:
                grid[i][j] = -1
                lightCount += 1
            if grid[i][j] == 1:
                isOn = True
            if grid[i][j] == 2:
                isOn = False
    print(lightCount)
 
 
 
# region fastio
 
BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
if __name__ == "__main__":
    main()