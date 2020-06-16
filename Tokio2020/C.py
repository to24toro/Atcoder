N,K = map(int,input().split())
A = list(map(int,input().split()))

for i in range(K):
    lis = [0]*(N+1)
    for j in range(N):
        lis[min(N,j+A[j]+1)] -= 1
        lis[max(0,j-A[j])] += 1
    cnt = 0
    for j in range(N):
        cnt += lis[j]
        A[j] = cnt
    cnt2 = 0
    for j in range(len(A)):
        if A[j] == N:
            cnt2 += 1
    if cnt2==N:
        break
print(' '.join(map(str,A)))
