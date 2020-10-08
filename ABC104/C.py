d,g = map(int,input().split())
info = []
for i in range(d):
    p,c = map(int,input().split())
    info.append([100*(i+1),p,c])
ans = float('inf')
for i in range(1,1<<d):
    cur = []
    for j in range(d):
        if (i>>j)&1:
            cur.append(info[j])
    cur.sort()
    for j in range(2):
        target = g
        res = 0
        for point,cnt,bonus in cur:
            if target <=0: break
            s = min(target//point,cnt)
            target -= s*point
            if s==cnt:
                target -= bonus
            res += s
        if target <=0:
            ans = min(ans,res)
        cur = cur[::-1]
print(ans)