n = int(input())
D = [None]*(n+1)
D[0] = [0]*(n+1)
from itertools import accumulate
for i in range(n):
    D[i+1] = [0] + [*accumulate(list(map(int, input().split())))]

for i in range(n):
    for j in range(n+1):
        D[i+1][j] += D[i][j]
cnt = [0]*(n**2+1)

for a in range(n+1):
    for b in range(n+1):
        for c in range(a+1,n+1):
            for d in range(b+1,n+1):
                x = D[c][d]-D[a][d]-D[c][b]+D[a][b]
                s = (c-a)*(d-b)
                cnt[s] = max(cnt[s],x)
q = int(input())

for i in range(q):
    p = int(input())
    print(max(cnt[:p+1]))