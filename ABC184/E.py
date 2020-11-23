import os
import sys
from io import BytesIO, IOBase
 
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
 

h,w = map(int,input().split())
S = [input() for _ in range(h)]
import collections
from collections import deque
d = [list() for _ in range(26)]
for i in range(h):
    for j in range(w):
        if S[i][j] =='S':
            s = [i,j]
        elif S[i][j]=='G':
            g = [i,j]
        elif S[i][j].islower():
            d[ord(S[i][j]) - 97].append((i, j))
dist = [[float('inf')]*w for _ in range(h)]

q = deque([(s[0],s[1],0)])
dist[s[0]][s[1]] = 0
seen = [False]*26
while q:
    x,y,c = q.popleft()
    if S[x][y].islower() and not seen[ord(S[x][y])-97]:
        seen[ord(S[x][y])-97] = True
        for i,j in d[ord(S[x][y]) - 97]:
            if i!=x or j!=y:
                if dist[i][j]>c+1:
                    dist[i][j] = c+1
                    q.appendleft((i,j,c+1))
    for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
        X  =x+dx
        Y = y+dy
        if 0<=X<h and 0<=Y<w and S[X][Y] != '#' and c+1<dist[X][Y]:
            dist[X][Y] = c+1
            q.append((X,Y,c+1))
    
print(dist[g[0]][g[1]] if dist[g[0]][g[1]]!=float('inf') else -1)
