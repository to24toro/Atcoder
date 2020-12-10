d = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
ans = float('inf')
for i in range(d):
    cnt += A[i]
    if cnt >=B[i]:
        ans = min(ans,B[i])
print(-1 if ans ==float('inf') else ans)