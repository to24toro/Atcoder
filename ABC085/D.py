N,H = map(int,input().split())
A = []
B = []
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
from bisect import bisect_right
val = A[-1]
idx = bisect_right(B,val)
B= B[idx:]
cnt = 0
while B and H:
    H-=B.pop()
    cnt += 1
    if H<=0: print(cnt);exit()
cnt += H//val
cnt += 1 if H%val else 0
print(cnt)