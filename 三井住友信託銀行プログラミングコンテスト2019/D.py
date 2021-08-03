n = int(input())
S = input()
ans = 0
from collections import defaultdict
from bisect import bisect_right
dic = defaultdict(list)
for i,s in enumerate(S):
    dic[int(s)].append(i)

for i in range(10):
    if len(dic[i])==0:
        continue
    ii = dic[i][0]
    for j in range(10):
        if len(dic[j])==0:
            continue
        jj = bisect_right(dic[j],ii)
        if jj==len(dic[j]):
            continue
        jj = dic[j][jj]
        for k in range(10):
            if len(dic[k])==0:
                continue
            kk = bisect_right(dic[k],jj)
            if kk != len(dic[k]):
                # print(i,j,k,ii,jj,kk)
                ans += 1
print(ans)
