s,p = map(int,input().split())
import math
A = []
for i in range(1,int(p**0.5)+1):
    if p%i==0:
        A.append(i)
        if i!=p//i:
            A.append(p//i)
for a in A:
    if a + p//a==s:
        print('Yes')
        exit()
print('No')