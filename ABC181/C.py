n = int(input())
L = []
for _ in range(n):
    x,y = map(int,input().split())
    L.append((x,y))
# print(1==1.000)
for i in range(n):
    for j in range(i+1,n):
        if L[i][0]==L[j][0]:
            for k in range(j+1,n):
                if L[i][0]==L[k][0]:
                    print('Yes');exit()
        else:
            for k in range(j+1,n):
                if L[k][1] ==(L[i][1] + (L[k][0]-L[i][0])*(L[j][1]-L[i][1])/(L[j][0]-L[i][0])):
                    print('Yes');exit()
print('No')
