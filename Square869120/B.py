n = int(input())
A = []
B = []
dist = 0
for _ in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    dist += abs(a-b)
A.sort()
B.sort()
if n%2:
    s,t = A[n//2],B[n//2]
else:
    s,t = (A[n//2]+A[n//2-1])//2,(B[n//2]+B[n//2-1])//2
for i in range(n):
    dist += abs(A[i]-s)
    dist += abs(B[i]-t)
print(dist)
