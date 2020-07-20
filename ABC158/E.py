from collections import Counter
n,p = map(int,input().split())
S = input()
dp = [0]
mod = p
if p==2:
    ans =0
    for i in reversed(range(n)):
        if int(S[i])%2==0:
            ans += i+1
    print(ans);exit()
elif p==5:
    ans =0
    for i in reversed(range(n)):
        if int(S[i])%5==0:
            ans += i+1
    print(ans);exit()
for i in reversed(range(n)):
    dp.append(dp[-1]%mod + pow(10,n-1-i,mod)*int(S[i]))
    dp[-1]%=mod
count = Counter(dp)
ans = 0
for key,val in count.items():
    if val>=2:
        ans += val*(val-1)//2
print(ans)