n = int(input())
A = list(map(int,input().split()))
s = A[0]
cnt = 0
ans = 0
for i in range(1,n):
    if A[i-1]>=A[i]:
        cnt += 1
        ans = max(ans,cnt)
    else:
        cnt = 0
print(ans)
