n = int(input())
P = []
for _ in range(n):
    x,y,z = map(int,input().split())
    P.append((x,y,z))
d = [[0]*n for _ in range(n)]

def f(i,j):
    a,b,c = P[i]
    p,q,r = P[j]
    return abs(p-a)+abs(q-b) + max(0,r-c)
def tsp(d):
    n = len(d)
    DP = dict()
    for A in range(1, 1 << n):
        if A & 1 << 0 == 0:
            continue
        if A not in DP:
            DP[A] = dict()
        for v in range(n):
            if A & 1 << v == 0:
                if A == 1 << 0:
                    DP[A][v] = d[0][v] if d[0][v] > 0 else float('inf')
                else:
                    DP[A][v] = min([DP[A ^ 1 << u][u] + d[u][v] for u in range(n) 
                                    if u != 0 and A & 1 << u != 0 and d[u][v] > 0]
                                  + [float('inf')])
    V = 1 << n
    DP[V] = dict()
    DP[V][0] = min([DP[A ^ 1 << u][u] + d[u][0] for u in range(n) 
                    if u != 0 and A & 1 << u != 0 and d[u][0] > 0]
                    + [float('inf')]) 


    return DP[V][0]

for i in range(n):
    for j in range(n):
        d[i][j] = f(i,j)
res = tsp(d)
print(res)