import math
n = int(input())
A = []
B = []
X,Y = 0,0
for _ in range(n):
    x,y = map(int,input().split())
    A.append((x,y))
    X += x
    Y += y
a_c = [X/n,Y/n]
d_a = 0
for x,y in A:
    d = (a_c[0]-x)**2 + (a_c[1]-y)**2
    d_a = max(d,d_a)
X,Y = 0,0
for _ in range(n):
    x,y = map(int,input().split())
    B.append((x,y))
    X += x
    Y += y
b_c = [X/n,Y/n]
d_b = 0
for x,y in B:
    d = (b_c[0]-x)**2 + (b_c[1]-y)**2
    d_b = max(d,d_b)
print(math.sqrt(d_b/d_a))
