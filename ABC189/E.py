def mat_mul(a,b):
    I,J,K = len(a),len(b[0]),len(b)
    c = [[0]*J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k]*b[k][j]
    return c

n = int(input())
L = []
for _ in range(n):
    x,y, = map(int,input().split())
    L.append((x,y,1))
A = [[0,1,0],[-1,0,0],[0,0,1]]
B = [[0,-1,0],[1,0,0],[0,0,1]]
E = [[[1,0,0],[0,1,0],[0,0,1]]]
m = int(input())
ans = []
for _ in range(m):
    op = list(map(int,input().split()))
    if op[0]==1:
        t = mat_mul(A,E[-1])
    elif op[0] ==2:
        t = mat_mul(B,E[-1])
    elif op[0] ==3:
        C = [[-1,0,op[1]*2],[0,1,0],[0,0,1]]
        t = mat_mul(C,E[-1])
    else:
        C = [[1,0,0],[0,-1,op[1]*2],[0,0,1]]
        t = mat_mul(C,E[-1])
    E.append(t)
q = int(input())
for _ in range(q):
    a,b = map(int,input().split())
    b-=1
    res = [0,0,0]
    e = E[a]
    l = L[b]
    for i in range(3):
        for j in range(3):
            res[i] += e[i][j]*l[j]
    ans.append(res)
for x,y,z in ans:
    print(x,y)
# for _ in range(m):
#     op = list(map(int,input().split()))
#     if op[0]==1:
#         tmp = mat_mul(A,E[-1])
#     elif op[0]==2:
#         tmp = mat_mul(B,E[-1])
#     elif op[0]==3:
#         C = [[-1,0,op[1]*2],[0,1,0],[0,0,1]]
#         tmp = mat_mul(C,E[-1])
#     else:
#         C = [[1,0,0],[0,-1,op[1]*2],[0,0,1]]
#         tmp = mat_mul(C,E[-1])
#     E.append(tmp)
# q = int(input())
# ans = []
# for _ in range(q):
#     a,b = map(int,input().split())
#     b-=1
#     e =E[a]
#     l = L[b]
#     res = [0,0,0]
#     for i in range(3):
#         for j in range(3):
#             res[i]+=e[i][j]*l[j]
#     ans.append(res)
# for x,y,_ in ans:
#     print(x,y)