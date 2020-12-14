a,b,c,d,t,v = map(int,input().split())
n = int(input())
import math
f = False
for i in range(n):
    x,y = map(int,input().split())
    d1 = math.sqrt((a-x)**2+(b-y)**2)
    d2 = math.sqrt((c-x)**2+(d-y)**2)
    if d1+d2<=t*v:
        f = True
print('YES' if f else 'NO')