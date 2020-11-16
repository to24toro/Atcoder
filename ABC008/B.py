n = int(input())
import collections
ans = 0
dic = collections.defaultdict(int)
for _ in range(n):
    s = input()
    dic[s]+=1
    if dic[ans]<dic[s]:
        ans = s
print(ans)