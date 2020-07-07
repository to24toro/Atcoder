N = int(input())
p = []
n = []
for i in range(N):
    end = 0
    mim = 0
    for c in input():
        if c=='(':
            end += 1
        else:
            end -= 1
        mim = min(min,end)
    if end >= 0:
        p.append([mim,end])
    else:
        n.append([end-mim,end])
p.sort(reverse=True)
n.port(reverse=True)
c = 0
f = True
for i in range(len(p)):
    if c+p[i][0]>=0:
        c += p[i][1]
    else:
        f = False
        break
for i in range(len(n)):
    if c +n[i][1]-n[i][0]>=0:
        c += n[i][1]
    else:
        f = False
        break

if c ==0 and f:
    f = True
else:
    f = False
print('Yes' if f else 'No')
