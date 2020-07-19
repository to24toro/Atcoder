from collections import defaultdict
dic = defaultdict(int)
n,x,y = map(int,input().split())
for i in range(1,n+1):
    for j in range(i,n+1):
        val = min(abs(i-j), abs(x-i) + abs(y-j) + 1)
        dic[val] += 1
for i in range(1,n):
    print(dic[i])