mod = 10**9+7
L = input()
dp1 = [0]*(len(L)+1)
dp2 = [0]*(len(L)+1)

dp2[0] = 1
for i in range(len(L)):
    dp1[i+1] = 3*dp1[i]
    if L[i]=='1':
        dp1[i+1] += dp2[i]
        dp2[i+1]=2*dp2[i]
    else:
        dp2[i+1] += dp2[i]
    dp1[i+1]%=mod
    dp2[i+1]%=mod
print((dp1[-1]+dp2[-1])%mod)
