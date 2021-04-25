n = int(input())
P = list(map(int,input().split()))
A = [0]*n
B = [0]*n
s = n**2
idx = P[0]
for i,p in enumerate(P):
    A[p-1] = s + (p-1-idx)*n +i
    B[p-1] = s - (p-1-idx)*n
print(*A)
print(*B)