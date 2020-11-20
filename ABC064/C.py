n = int(input())
A = list(map(int,input().split()))
from collections import defaultdict
dic = defaultdict(int)
cnt = 0
for a in A:
    if a<3200:
        dic[a//400]+=1
    else:
        cnt += 1
if len(dic)==0:
    print(1,min(cnt,8));exit()

print(len(dic),len(dic)+cnt)