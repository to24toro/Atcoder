from collections import defaultdict
N, _K = input().split()
K = int(_K)
INF = K + 1
dp = defaultdict(int)
eq_prod = 1


for i in range(len(N)):
    digit = ord(N[i])-ord('0')
    nxt = defaultdict(int)


    for prod,val in dp.items():
        for d in range(10):
            nxt_prod = min(INF,prod*d)
            nxt[nxt_prod] += val
    
    for d in range(digit):
        if i==0 and d == 0:
            continue
        nxt_prod = min(INF,eq_prod*d)
        nxt[nxt_prod] += 1
    
    eq_prod = min(INF,eq_prod*digit)

    if i!=0:
        for d in range(1,10):
            nxt_prod = min(INF,d)
            nxt[nxt_prod] += 1
    dp = nxt


ans = 0

for prod,val in dp.items():
    if prod<=K:
        ans += val

if eq_prod<=K:
    ans += 1

print(ans)



######################################################

from collections import defaultdict
N, K = map(int, input().split())
digit = len(str(N))
li = [int(s) for s in str(N)]
dp = [[defaultdict(int) for _ in range(2)] for _ in range(digit)]
dp[0][1][li[0]] += 1
for top in range(1, li[0]):
    dp[0][0][top] += 1

for i in range(1,len(li)):
    top = li[i]

    for k in range(10):
        for key,val in dp[i-1][0].items():
            dp[i][0][key*k] += val
    
    for k in range(1,10):
        dp[i][0][k] += 1
    
    for k in range(top):
        for key,val in dp[i-1][1].items():
            dp[i][0][key*k] += val
    
    for key,val in dp[i-1][1].items():
        dp[i][1][top*key] += val

ans = 0

for key, val in dp[-1][0].items():
    if key<=K:
        ans += val

for key, val in dp[-1][1].items():
    if key<=K:
        ans += val

print(ans)


##############################################
from collections import defaultdict
N, K = map(int, input().split())
memo = defaultdict(int)
def dp(n,k):
    if memo[(n,k)]:
        return memo[(n,k)]
    res = (k>0) + n//10
    for y in range(1,min(10,n+1)):
        res += dp((n-y)//10,k//y)
    memo[(n,k)] = res
    return res
print(dp(N,K)-1)
