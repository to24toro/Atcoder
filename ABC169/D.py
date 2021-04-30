S = input()
mod = 2019
from collections import defaultdict
dic = defaultdict(int)
n = len(S)
a=0
dic[0]+=1
ans = 0
for i in range(n):
    a += pow(10,i,mod)*int(S[n-i-1])
    a%=mod
    dic[a]+=1
for k,v in dic.items():
    if v>1:
        ans += v*(v-1)//2
# print(dic)
print(ans)
