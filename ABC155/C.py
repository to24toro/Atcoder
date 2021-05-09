n = int(input())
from collections import defaultdict
dic = defaultdict(int)
for _ in range(n):
    s = input()
    dic[s]+=1
ans = sorted(dic.items(), key = lambda x:[-x[1],x[0]])
mx = ans[0][1]
for k,v in ans:
    if v==mx:
        print(k)