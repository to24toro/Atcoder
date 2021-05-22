A = list(map(int,input().split()))
A.sort()
if A[1]*2 ==A[2]+A[0]:
    print('Yes')
else:
    print('No')