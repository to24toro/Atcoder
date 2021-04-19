h,w,x,y = map(int,input().split())
S = [input() for _ in range(h)]
x-=1
y-=1
ans = 0
cnt = 0
for i in range(x+1,h):
    if S[i][y]=='.':
        cnt+=1
    else:
        break

ans += cnt
cnt = 0
for i in range(x-1,-1,-1):
    if S[i][y]=='.':
        cnt+=1
    else:
        break

ans += cnt
cnt = 0
for i in range(y+1,w):
    if S[x][i]=='.':
        cnt+=1
    else:
        break

ans += cnt

cnt = 0
for i in range(y-1,-1,-1):
    if S[x][i]=='.':
        cnt+=1
    else:
        break

ans += cnt
print(ans+1)