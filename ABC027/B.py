n = int(input())
A = list(map(int,input().split()))
s = sum(A)
t = s/n
if not t.is_integer():print(-1);exit()
t =int(t)
ans = 0
cnt = 0
cur = 0
for i in range(n):
    cnt += 1
    cur += A[i]
    if cur ==t*cnt:
        cnt = 0
        cur = 0
    else:
        ans +=1
print(ans)