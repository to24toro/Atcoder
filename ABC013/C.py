n,h = map(int,input().split())
a,b,c,d,e = map(int,input().split())
ans = float('inf')
import math
if h>n*e:print(0);exit()
for x in range(n+1):
    y = ((n-x)*e-h-b*x)//(d+e)
    y += 1
    y = max(0,y)
    ans = min(ans,a*x+c*y)
print(ans)