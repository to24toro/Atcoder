n,k = map(int,input().split())
S = []
dp = []
cnt = 1
for _ in range(n):
    s = int(input())
    S.append(s)
if S.count(0):print(n);exit()

s,t = 0,0
cnt = 1
ans = 0
while s<=t and t<n:
    if cnt*S[t] <=k:
        cnt *=S[t]
        t += 1
    else:
        cnt//=S[s]
        s += 1
    ans = max(ans,t-s)
print(ans)