n,t = map(int,input().split())
L = []
m = 0
for _ in range(n):
    a,b = map(int,input().split())
    m = max(b,m)
    L.append((a,b))
L.sort()
dp =[[0]*(t+m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(t+m+1):
        if j-L[i][0]>=0 and t>j-L[i][0]:
            dp[i+1][j] = max(dp[i][j],dp[i][j-L[i][0]]+L[i][1])
        else:
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
ans = 0
for i in range(n+1):
    ans = max(ans,max(dp[i]))

print(ans)
#     L.append((b/a,a,b))
# L.sort(key = lambda x:(-x[0],x[1]))
# hq = []
# ans = []
# print(L)
# import heapq
# for c,a,b in L:
#     if a>=t:
#         heapq.heappush(hq,(-b,a,c))
#     else:
#         ans.append((b,a,c))
#         t-=a
# heapq.heapify(ans)
# if t ==0 and hq:
#     nb,nc,na = heapq.heappop(hq)
#     bb,bc,ba = heapq.heappop(ans)
#     if nb>bb:
#         heapq.heappush(ans,(-nb,nc,na))
#     else:
#         heapq.heappush(ans,(bb,b,c,ba))
# elif hq:
#     nb,nc,na = heapq.heappop(hq)
#     heapq.heappush(ans,(-nb,nc,na))
# res = 0
# for b,c,a in ans:
#     res += b
# print(ans)


