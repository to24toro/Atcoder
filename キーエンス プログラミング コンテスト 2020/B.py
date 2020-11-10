n = int(input())
L = []
for _ in range(n):
    x,l = map(int,input().split())
    L.append((x-l,x+l))
cnt = n
L.sort(key = lambda x:x[1])
s = L[0][1]
for i in range(1,n):
    if L[i][0]<s:
        cnt-=1
    else:
        s = L[i][1]
print(cnt)