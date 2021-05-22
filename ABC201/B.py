n = int(input())
L=  [list(map(str,input().split())) for _ in range(n)]
for i in range(n):
    L[i][1] = int(L[i][1])
L.sort(key = lambda x:-x[1])
print(L[1][0])