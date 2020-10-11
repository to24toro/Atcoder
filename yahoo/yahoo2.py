n,k = map(int,input().split())
P = []
T = []

for i in range(n):
    p = input()
    if p!='read':
        p = p.split(' ')
        T.append([int(p[-1]),i])
        P.append(int(p[-1]))
    else:
        P.append(p)
T.sort(reverse = True)
for i in range(n):
    if P[i]=='read':
        for j in range(len(T)):
            t,day = T[j]
            if day+k<i:
                T[j][1] = i
                print(t)
                break
    else:
        print(P[i])

