n = int(input())
l,r = 0,0
cnt = 0
ans = []
for bit in range(1<<n):
    l,r = 0,0
    cnt = 0
    f =True
    for i in range(n):
        if (bit>>i)&1:
            l+=1
            cnt += 1
        else:
            r += 1
            cnt-=1
        if cnt<0:
            f = False

    if l==r and f:
        ans.append(bit)
# print(len(ans))
res = []
for a in ans:
    tmp = ""
    for i in range(n):
        if (a>>i)&1:
            tmp+='('
        else:
            tmp +=')'
    res.append(tmp)
res.sort()
for r in res:
    print(r)