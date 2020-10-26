n,m,x,y = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
X.sort()
Y.sort()
for i in range(x+1,y+1):
    if i>X[-1] and i<=Y[0]:
        print('No War')
        exit()
print('War')