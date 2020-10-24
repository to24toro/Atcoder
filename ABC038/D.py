from bisect import bisect_right
INF=float('inf')
  
n=int(input())
B=[]
for _ in range(n):
  w,h=map(int,input().split())
  B.append([w,h])
B.sort(key=lambda x:[x[0],-x[1]])
dp=[INF]*(n+1)
dp[0]=-1
for i in range(n):
  idx=bisect_right(dp,B[i][1]-1)
  dp[idx]=min(B[i][1],dp[idx])
ans=-INF
for j in range(n+1):
  if dp[j]<INF:
    ans=max(ans,j)
print(ans)