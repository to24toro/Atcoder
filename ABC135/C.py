n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
for i in range(n):
    v=min(A[i],B[i])
    cnt +=v
    B[i]-=v
    plus = A[i+1] if B[i]>=A[i+1] else B[i]
    A[i+1]= 0 if B[i]>=A[i+1] else A[i+1]-B[i]
    cnt += plus
print(cnt)