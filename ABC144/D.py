a,b,x = map(int,input().split())
s = a*a*b

import math
if x<=s/2:
    ans = math.degrees(math.atan((a*b*b)/(2*x)))
else:
    ans = math.degrees(math.atan(2*(a*a*b-x)/(a**3)))
print(ans)
