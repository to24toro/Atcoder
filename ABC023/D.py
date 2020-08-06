n = int(input())
Balloon= []
m = 0
for _ in range(n):
    h,s = map(int,input().split())
    Balloon.append((h,s))
    m = max(m,h+n*s)
l,r = 0,m
while l<=r:
    mid = (l+r)//2
    tmp = []
    for h,s in Balloon:
        tmp.append((mid-h)/s)
    tmp.sort()
    if tmp[0]<0:
        l = mid+1
    else:
        flag = True
        for i,x in enumerate(tmp):
            if i>x:
                flag = False
        if flag:
            r = mid-1
        else:
            l = mid+1
print(l)
        
