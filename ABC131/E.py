n,k = map(int,input().split())
val = (n-1)*(n-2)//2
if k > val:print(-1);exit()


print(n-1+val-k)

for i in range(2,n+1):
    print('1' + ' ' + str(i))

v = 2
w = 3
while k < val:
    val -= 1
    print(v, w)
    w += 1
    if w == n + 1:
        v += 1
        w = v + 1