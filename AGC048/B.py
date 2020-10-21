n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
odd = []
even = []

for i in range(n):
    if i%2:
        odd.append([i,A[i]-B[i]])
    else:
        even.append([i,A[i]-B[i]])
odd.sort(key = lambda x:-x[1])
even.sort(key = lambda x:-x[1])
from collections import deque
p = deque(odd)
q = deque(even)
tmp = sum(B)
dp= sum(B)
n //=2
for i in range(1,n+1):
    a = p.popleft()
    b = q.popleft()
    tmp += a[1] + b[1]
    dp = max(dp,tmp)
print(dp)