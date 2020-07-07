X = int(input())
from math import pow
for a in range(-120,120,1):
    for b in range(-120,120,1):
        if pow(a,5)-pow(b,5)==X:
            print(a,b);exit()