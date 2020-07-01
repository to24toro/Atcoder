N = int(input())
A = []
B = []
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if N%2==1:
    print(B[int(N-1)//2]-A[int(N-1)//2]+1)
else:
    print(B[(N-1)//2]-A[(N-1)//2]+B[1+(N-1)//2]-A[1+(N-1)//2]+1)