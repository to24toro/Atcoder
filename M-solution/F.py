n = int(input())
X = []
Y = []
D = []
for _ in range(n):
    x,y,d = map(int,input().split())
    X.append(x)
    Y.append(y)
    D.append(d)

def rotate():
    for i in range(n):
        cx,cy = Y[i],200000-X[i]
        if D[i]=='U': cz = 'R'
        if D[i]=='R': cz = 'D'
        if D[i]=='D': cz = 'L'
        if D[i]=='L': cz = 'U'
        X[i],Y[i],D[i] = cx,cy,cz

def solve():
    ans = float('inf')
    