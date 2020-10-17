x,y,a,b = map(int,input().split())
import math
cnt = 0
while x<=b/(a-1):
    if a*x>=y:
        break
    else:
        cnt += 1
        x *=a

d  =(y-x)//b
if (y-x)%b==0:
    print(cnt+d-1)
else:
    print(cnt+d)