#ワーシャルフロイド
v,e = map(int,input().split())
d = [[float('inf')]*v for _ in range(v)]
for _ in range(e):
    s,t,D = map(int,input().split())
    d[s][t] = D
for i in range(v):
    d[i][i] = 0

for k in range(v):
    for i in range(v):
        for j in range(v):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])
for i in range(v):
    if d[i][i]<0:
        print('NEGATIVE CYCLE');exit()
for l in d:
    tmp = []
    for i in l:
        if i==float('inf'):
            tmp.append('INF')
        else:
            tmp.append(str(i))
    print(' '.join(tmp))