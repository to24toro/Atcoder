from itertools import permutations
p = [0]*15
m = [0]*15
v = [0,1,2,3,4,5,6,7]
h = [0,1,2,3,4,5,6,7]
k = int(input())
Q = [[',']*8 for _ in range(8)]
# print(Q)
for _ in range(k):
    a,b = map(int,input().split())
    h.remove(a)
    v.remove(b)
    p[a+b] = 1
    m[7+a-b] = 1
    Q[a][b] = 'Q'
    
for l in permutations(col):
    for r, c in zip(row, l):
        print(r,c)
def show():
    for i in range(8):
        print(''.join(Q[i]))



