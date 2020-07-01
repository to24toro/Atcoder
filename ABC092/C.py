N = int(input())
A = list(map(int,input().split()))
A = [0] + A + [0]
B = []
for i in range(1,len(A)):
    B.append(abs(A[i]-A[i-1]))
S = sum(B)
for i in range(N):
    print(S-abs(A[i]-A[i+1])-abs(A[i+1]-A[i+2])+abs(A[i]-A[i+2]))
