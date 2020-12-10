n,m = map(int,input().split())
x,y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
from bisect import bisect_left
s = ['A',A[0]]
cnt = 0
while True:
    if s[0]=='A':
        idx = bisect_left(B,s[1]+x)
        if idx==len(B):
            break
        else:
            cnt += 1
            s = ['B',B[idx]]
    else:
        idx = bisect_left(A,s[1]+y)
        if idx ==len(A):
            break
        else:
            s = ['A',A[idx]]
print(cnt)