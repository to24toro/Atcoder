n = int(input())
from math import cos,sin,pi

pi = pi
theta = pi*(n-2)/(2*n)
x,y = map(int,input().split())
a,b = map(int,input().split())
X = a-x
Y = b-y
X*=cos(theta)
Y*=cos(theta)
# print(X,Y)

xx = X*cos(theta)+Y*sin(theta)
yy = -X*sin(theta)+Y*cos(theta)
# print(xx,yy)
print(xx+x,yy+y)