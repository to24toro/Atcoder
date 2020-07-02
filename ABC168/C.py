A,B,H,M = map(int,input().split())

import math

minute = math.pi*2*M/60
hour = math.pi*2*H/12 + math.pi*(1/6)*M/60

cos = math.cos(abs(hour-minute))

ans = math.sqrt(A**2+B**2-2*A*B*cos)

print(ans)