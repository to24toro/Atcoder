n,m,d = map(int,input().split())
A = list(map(int,input().split()))

L = [i for i in range(n)]
for a in A:
    L[a-1],L[a] = L[a],L[a-1]

dp = [[0]*n for _ in range(31)]

dp[0] = L

for i in range(30):
    for j in range(n):
        dp[i+1][j] = dp[i][dp[i][j]]
A = [i for i in range(n)]

for i in range(30):
    if (d>>i)&1:
        for j in range(n):
            A[j] = dp[i][A[j]]
ans = [0]*n

for i in range(n):
    ans[A[i]] = i

for a in ans:
    print(a+1)
