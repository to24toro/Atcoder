import math
n = int(input())
set1 = set()
set2 = set()
L = []
T = []
for _ in range(n):
    x,y = map(int,input().split())
    T.append((x,y))
    if x not in set1:
        set1.add(x)
        L.append((x,100))
    if x not in set2:
        set2.add(x)
        L.append((x,-100))
def dist(i,j):
    x1,y1 = L[i]
    x2,y2 = L[j]
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

T.sort()

