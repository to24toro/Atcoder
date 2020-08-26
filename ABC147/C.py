n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x,y = map(int,input().split())
        g[i].append((x-1,y))
ans = 0
for bit in range(1<<n):
    f = True
    for i in range(n):
        if bit&(1<<i) and f:
            for x,y in g[i]:
                if y ==1 and bit&(1<<x):
                    continue
                elif y ==0 and bit&(1<<x)==0:
                    continue
                else:
                    f = False
                    break
    if f:
        ans = max(ans,bin(bit).count('1'))
print(ans)
