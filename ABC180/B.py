n = int(input())
X = list(map(int,input().split()))
Y  =[]
for x in X:
    Y.append(abs(x))
d = 0
for y in Y:
    d += y**2
import math

print(sum(Y))
print(math.sqrt(d))
print(max(Y))