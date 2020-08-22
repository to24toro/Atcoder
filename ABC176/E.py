h,w,m = map(int,input().split())
H = [set() for _ in range(h)]
W = [set() for _ in range(w)]
cord = []
for _ in range(m):
    a,b = map(int,input().split())
    H[a-1].add(b-1)
    W[b-1].add(a-1)
    cord.append((a-1,b-1))
X = 0
set_x = set()
for i in range(h):
    if X<len(H[i]):
        X = len(H[i])
        set_x= set()
        set_x.add(i)
    elif X ==len(H[i]):
        set_x.add(i)

    
Y = 0
set_y = set()
for i in range(w):
    if Y<len(W[i]):
        Y = len(W[i])
        set_y = set()
        set_y.add(i)
    elif Y ==len(W[i]):
        set_y.add(i)
# print(set_x,set_y,X,Y)
n = len(set_x)*len(set_y)
for x,y in cord:
    if x in set_x and y in set_y:
        n -=1
if n:
    cnt =0
else:
    cnt = -1

print(X+Y+cnt)
