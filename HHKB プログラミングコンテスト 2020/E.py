h,w = map(int,input().split())
L = [list(input()) for _ in range(h)]
k = 0
for i in range(h):
    for j in range(w):
        if L[i][j]=='.':
            k +=1
mod = 10**9+7
ans = pow(2,k,mod)*k
dist = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(h):
    for j in range(w):
        if L[i][j]=='.':
            t = 1
            for x,y in dist:
                if 0<=i+x<h and 0<=j+y<w and L[i+x][j+y]=='.':
                    t += 1
            ans -=pow(2,k-t,mod)

print(ans%mod)
