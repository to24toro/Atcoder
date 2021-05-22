n,m = map(int,input().split())
AA = list(map(int,input().split()))
from functools import lru_cache
dic = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
dp = [None]*(n+1)
A = []
for a in AA:
    A.append((dic[a],a))
A.sort()
dp[0] = ""
for i in range(2,n+1):
    for _,a in A:
        if i-dic[a]>=0:
            if dp[i-dic[a]]:
                if dp[i] is None:
                    dp[i]=dp[i-dic[a]]+str(a)
                else:
                    if len(dp[i])<=len(dp[i-dic[a]])+1:
                        dp[i] = dp[i-dic[a]]+str(a)
print(dp)