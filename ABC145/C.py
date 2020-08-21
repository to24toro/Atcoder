from itertools import permutations
import math
n = int(input())
A = []
for _ in range(n):
    x,y = map(int,input().split())
    A.append([x,y])
tmp = 0
cnt = 0
for L in permutations(A):
    cnt += 1
    for i in range(1,len(L)):
            tmp += math.sqrt((L[i][0]-L[i-1][0])**2+(L[i][1]-L[i-1][1])**2)
print(tmp/cnt)
    