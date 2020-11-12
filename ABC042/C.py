n,k = map(int,input().split())
D = set(map(str,input().split()))
for i in range(n,100000):
    s = str(i)
    f = True
    for j in s:
        if j in D:
            f = False
            break
    if f:
        print(i);exit()
