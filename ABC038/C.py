n = int(input())
A = list(map(int,input().split()))
cnt = 1
ans = 1
if n==1:
    print(1);exit()
for i in range(1,n):
    if A[i]>A[i-1]:
        cnt += 1
        ans += cnt
    else:
        cnt = 1
        ans += cnt
print(ans)

