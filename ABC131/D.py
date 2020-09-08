n = int(input())
L = []
for _ in range(n):
    a,b = map(int,input().split())
    L.append((a,b))
L.sort(key = lambda x:(x[1],x[0]))
cur = 0
for a,b in L:
    if cur +a >b:
        print('No');exit()
    cur += a
print('Yes')