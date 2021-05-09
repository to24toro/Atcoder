h,w = map(int,input().split())
A = [input() for _ in range(h)]

H = set()
W = set()
for i in range(h):
    for j in range(w):
        if A[i][j]=="#":
            H.add(i)
            W.add(j)
ans = []
for i in range(h):
    if i in H:
        tmp = ''
        for j in range(w):
            if j in W:
                tmp+=A[i][j]
        ans.append(tmp)
for a in ans:
    print(a)

