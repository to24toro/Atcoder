
#da[i][j]:(0,0)~(i,j)の長方形の和
def da_generate(h,w,a):
    da = [[0]*w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1,w):
        da[0][i] = da[0][i-1]+a[0][i]
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i-1][j]+cnt_w
    return da

#da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和(p,q)を含む
def da_calc(p,q,x,y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y]-da[x][q-1]
    if q == 0:
        return da[x][y]-da[p-1][y]
    return da[x][y]-da[p-1][y]-da[x][q-1]+da[p-1][q-1]

n = int(input())
D = [list(map(int,input().split())) for _ in range(n)]
da = da_generate(n,n,D)
# print(da)
# print(da_calc(0,0,0,0))
q = int(input())
from collections import defaultdict
dic = defaultdict(int)
for x1 in range(n):
    for x2 in range(x1,n):
        for y1 in range(n):
            for y2 in range(y1,n):
                s = (x2-x1+1)*(y2-y1+1)
                val = da_calc(x1,y1,x2,y2)
                # print(s,val)
                dic[s] = max(dic[s],val)
P = [0]
for i in range(1,n**2+1):
    P.append(max(P[-1],dic[i]))
# print(P)
for _ in range(q):
    p = int(input())
    print(P[p])