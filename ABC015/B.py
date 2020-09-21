n = int(input())
A = list(map(int,input().split()))
ans = 0
cnt = 0
for a in A:
    if a !=0:
        cnt +=1
        ans += a
import math
if cnt ==0:print(0);exit()
print(math.ceil(ans/cnt))