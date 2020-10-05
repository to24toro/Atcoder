n,s = map(str,input().split())
n = int(n)
from collections import defaultdict
ans = 0
for i in range(n):
    cnt = defaultdict(int)
    cnt[s[i]] += 1
    for j in range(i+1,n):
        cnt[s[j]] += 1
        if cnt['A']==cnt['T'] and cnt['G']==cnt['C']:
            ans += 1
print(ans)