n,m = map(int,input().split())
S = input()
cnt = 0
for s in S:
    if s=='1':
        cnt+=1
    else:
        cnt = 0
    if cnt>=m:
        print(-1);exit()
if S[0]=='1' or S[-1]=='1':print(-1);exit()
T = S[::-1]
i,j = 0,0
cnt =0
ans = []
while i<n:
    j = 0
    step = i
    for j in range(1,m+1):
        if i+j<=n:
            if T[i+j]=='0':
                step = i+j
        else:
            break
    ans.append(step-i)
    # print(i,j)
    i = step
    cnt += 1
print(*ans[::-1])
