n,l = map(int,input().split())
v,d = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(n)]
X.append([l,0,0])
X.append([0,v,d])
X.sort(key = lambda x:x[0])
dp = [float('inf')]*(n+2)
dp[0] = 0
for i in range(1,n+2):
    for j in range(i):
        if X[i][0]-X[j][0]<=X[j][2]:
            dp[i] = min(dp[i],dp[j]+(X[i][0]-X[j][0])/X[j][1])
print(dp[-1] if dp[-1]!=float('inf') else 'impossible')