n = int(input())
A = list(map(int,input().split()))
cnt = 0
sum = A[0]
for i in range(1,n):
    if abs(sum)>=abs(A[i]):
        cnt += abs(sum+A[i]) + 1
        if sum>0:
            A[i] -=abs(sum+A[i]) + 1
        else:
            A[i] +=abs(sum+A[i]) + 1
    sum += A[i]
cnt2 = 0
sum = 1 if A[0] >=0
for i in range(1,n):
    if abs(sum)>=abs(A[i]):
        cnt += abs(sum+A[i]) + 1
        if sum>0:
            A[i] -=abs(sum+A[i]) + 1
        else:
            A[i] +=abs(sum+A[i]) + 1
    sum += A[i]
print(cnt)

