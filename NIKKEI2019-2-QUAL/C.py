n,k = map(int,input().split())
if 2*k>n+1:print(-1);exit()
for i in range((n+1)//2):
    print(k + (n+1) // 2 - 1 - i, k + n + 2*i, k + 2*n + i)
for i in range(n // 2):
    print(k + n - 1 - i, k + n + 1 + 2*i, k + 2*n + (n+1) // 2 + i)
