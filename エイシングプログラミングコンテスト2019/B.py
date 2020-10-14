n = int(input())
a,b = map(int,input().split())
P = list(map(int,input().split()))
x,y,z = [],[],[]
for p in P:
    if a>=p:x.append(p)
    elif a<p and p<=b:y.append(p)
    else:z.append(p)
print(min(len(x),len(y),len(z)))