n = int(input())
A = list(map(lambda x:int(x)-1,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = B[A[0]]
for i in range(1,n):
    ans += B[A[i]]
    if A[i]==A[i-1]+1:
        ans+=C[A[i-1]]
print(ans)