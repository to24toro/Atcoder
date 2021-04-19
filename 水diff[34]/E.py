n,T = map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(n)]
import copy
A.sort()
dp = [0]*T
ans = 0
dp2 = [0]*T
for a,b in A:
    for t in range(T):
        if t+a>=T:
            pass
        else:
            dp2[t+a] = max(dp[t+a],dp[t]+b)
        ans = max(ans,dp[t]+b)
    dp = copy.copy(dp2)
print(ans)



# n,t=map(int,input().split())
# from collections import defaultdict
# import copy
# dp=[1]+[0]*(t-1)
# dp_=[1]+[0]*(t-1)
# ans=0
# ab=[list(map(int,input().split())) for _ in range(n)]
# ab.sort()
# for a,b in ab:
#     for i in range(t):
#         if i+a>=t or dp[i]==0:
#             pass
#         else:
#             dp_[i+a]=max(dp[i+a],dp[i]+b)
#         ans=max(ans,dp[i]+b)
#     dp=copy.copy(dp_)
# print(ans-1)