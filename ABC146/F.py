n,m = map(int,input().split())
S = input()
ans = []
S = S[::-1]
pre = 0
i = 1
cnt = 0
while i<=n:
    cnt += 1
    if S[i]=='0':
        pre = cnt
    if cnt ==m:
        if pre==0:
            print(-1);exit()
        if S[i]=='0':
            ans.append(cnt)
            i+=1
        else:
            ans.append(pre)
            i-=cnt-pre-1
        cnt = 0
        pre = 0
    else:
        i+=1
if cnt!=0:
    ans.append(cnt)
ans.reverse()
print(*ans)