N,K = map(int,input().split())
A = list(map(int,input().split()))
from collections import defaultdict
dic = defaultdict(int)
for a in A:
    dic[a] += 1
sort_dic = sorted(dic.items(), key = lambda x:x[1])
n = len(sort_dic)
if n<=K: print(0);exit()
ans = 0
for i in range(n-K):
    ans += sort_dic[i][1]
print(ans)