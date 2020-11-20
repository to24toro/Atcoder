h,w = map(int,input().split())
S = [input() for _ in range(h)]
A = []
row = [False]*h
col = [False]*w
for i in range(h):
    for j in range(w):
        if S[i][j]=='#':
            row[i] = True
            col[j] = True
# print(row,col)
for i in range(h):
    if row[i]:
        for j in range(w):
            if col[j]:
                print(S[i][j], end ='')
        print()


