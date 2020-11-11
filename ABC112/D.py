n,m = map(int,input().split())
L = []
for i in range(1,int(m**0.5)+1):
    if m%i==0:
        L.append(i)
        if m//i==i:
            L.append(m//i)
L.sort()
res = 1
for l in L:
    tmp = m-n*l
    if tmp>=0 and tmp%l==0:
        res = l
print(res)

