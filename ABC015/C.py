n,k = map(int,input().split())
from itertools import product
t = [list(map(int,input().split())) for _ in range(n)]

for p in product(*t):
    cur = 0
    for i in range(n):
        cur ^=p[i]
    if cur ==0:
        print('Found');exit()
print('Nothing')