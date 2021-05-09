t,N = map(int,input().split())
import math
if (100*N)%t==0:
    a = (100*N)//t-1
else:
    a = 100*N//t
print(int((100+t)*a/100)+1)

