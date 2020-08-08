n,k = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
P = []
M = []
Z = []
for a in A:
    if a==0:Z.append(a)
    elif a>0:P.append(a)
    else: P.append(a)
p,m,z = len(P),len(M),len(Z)
if p*m>=k:
    P.sort(reverse=True)
    print(M[(k-1)//p]*P[(k-1)%p])
    exit()
else:
    if k<=p*m + z*(p+m) + z*(z-1)//2:
        print(0);exit()
    else:
        k-=p*m + z*(p+m)+ z*(z-1)//2
        
