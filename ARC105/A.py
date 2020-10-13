A = list(map(int,input().split()))
A.sort()
if sum(A[:3])==A[-1] or A[0]+A[-1]==A[2]+A[1]:
    print('Yes')
else:
    print('No')