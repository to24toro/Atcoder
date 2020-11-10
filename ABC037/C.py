n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = sum(A[:k])
cnt = ans
for i in range(k,n):
    cnt-=A[i-k]
    cnt += A[i]
    ans += cnt
print(ans)