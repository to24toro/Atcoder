n = int(input())
A = list(map(int,input().split()))
A.sort()
from collections import deque
q = deque(A)
s = (A[0] + A[1])/2
q.popleft()
q.popleft()
while q:
    t = q.popleft()
    s +=t
    s/=2
print(s)