n = int(input())
L = []
A,B,C = [],[],[]
for _ in range(n):
    a,b,c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    L.append([a,b,c])
if n ==1: print(max(L[0]));exit()

for i in range(1,n):
    A[i],B[i],C[i] = A[i]+max(B[i-1],C[i-1]),B[i]+max(A[i-1],C[i-1]),C[i] + max(A[i-1],B[i-1])

print(max(A[-1],B[-1],C[-1]))
    
