N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
from bisect import bisect_left,bisect_right
for b in B:
    ida = bisect_left(A,b)
    idc = bisect_right(C,b)
    ans += ida*(N-idc)
print(ans)
