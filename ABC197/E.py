n = int(input())
from collections import defaultdict
color = [0]*(2*10**5+1)
mx = [-float('inf')]*(2*10**5+1)
mn = [float('inf')]*(2*10**5+1)
for _ in range(n):
    x,c = map(int,input().split())
    color[c]=1
    mx[c] = max(mx[c],x)
    mn[c] = min(mn[c],x)

s = 0
pa = 0
pb = 0
ta = 0
tb = 0
for i in range(2*10**5+1):
    if color[i]==0:
        continue
    chk = i
    ta,tb = min(ta+abs(pa-mn[i]),tb+abs(pb-mn[i]))+abs(mx[i]-mn[i]),min(ta+abs(pa-mx[i]),tb+abs(pb-mx[i]))+abs(mx[i]-mn[i])
    pa = mx[i]
    pb = mn[i]
ta+=abs(mx[chk])
tb+=abs(mn[chk])
print(min(ta,tb))

