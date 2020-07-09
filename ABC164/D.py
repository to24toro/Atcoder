#0からiまでのSを2019で割ったときのあまりを調べる
#A%mod =a,B$mod=aなら（A-B)%mod=0
from collections import Counter
S = input()
dp = [0]
mod = 2019
for i in reversed(range(len(S))):
    dp.append(dp[-1]%mod+pow(10,len(S)-i-1,mod)*int(S[i]))
    dp[-1]%=mod
count = Counter(dp)
ans = 0
for key,val in count.items():
    if val>=2:
        ans += val*(val-1)//2
print(ans)