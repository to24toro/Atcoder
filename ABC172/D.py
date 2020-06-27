N = int(input())
import collections
dic = collections.defaultdict(int)
for i in range(1,N+1):
    for j in range(i,N+1,i):
        dic[j] += 1
ans = 0
for i in range(1,N+1):
    ans +=dic[i]*i
print(ans)