n = int(input())
A = list(map(int,input().split()))
if n ==1: print(0);exit()
cnt = 0
for i in range(1,n):
    if A[i]<A[i-1]:
        cnt += A[i-1]-A[i]
        A[i] = A[i-1]
        
print(cnt)
