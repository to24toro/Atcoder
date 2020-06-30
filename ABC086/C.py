A = [[0,0]]
N = int(input())
for _ in range(N):
    t,x,y = map(int,input().split())
    A.append([t,x+y])
for i in range(1,N+1):
    
    if A[i][0]-A[i-1][0] >= abs(A[i][1]-A[i-1][1]) and (A[i][0]-A[i-1][0])%2 == (A[i][1]-A[i-1][1])%2:
        continue
    else:
        print('No')
        exit()
print('Yes')
