N = int(input())
T = []
for _ in range(N-1):
    c,s,f = map(int,input().split())
    T.append([c,s,f])
for i in range(1,N):
    t =0
    for j in range(i-1,N-1):
        c,s,f = T[j]
        if t <=s: t =s+c
        elif t%f==0: t += c
        else: t += f -(t%f) + c
    print(t)

print(0)