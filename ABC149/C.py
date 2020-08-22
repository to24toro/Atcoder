x = int(input())
A = [0]*(2*10**5)
for i in range(2,len(A)):
    if A[i]==0:
        for j in range(2*i,len(A),i):
            A[j]=1
for i in range(x,len(A)):
    if A[i]==0:
        print(i);exit()