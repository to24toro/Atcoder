h,w = map(int,input().split())
S = []
for _ in range(h):
    s = input()
    S.append(s)
d = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(0,0)]
A = [['#']*w for _ in range(h)]
B = [['#']*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if S[i][j] =='.':
            for x,y in d:
                X = i+x
                Y = j + y
                if 0<=X<h and 0<=Y<w:
                    A[X][Y]='.'
                    B[X][Y]='.'
for i in range(h):
    for j in range(w):
        if A[i][j]=='#':
            for x,y in d:
                X = i+x
                Y = j + y
                if 0<=X<h and 0<=Y<w:
                    B[X][Y]='#'

for i in range(h):
    for j in range(w):
        if S[i][j]!=B[i][j]:
            print('impossible');exit()
print('possible')
for a in A:
    print(''.join(a))

