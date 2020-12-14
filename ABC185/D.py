n,m = map(int,input().split())
A= list(map(lambda x:int(x),input().split()))
A.append(0)
A.append(n+1)
if m==0:print(1);exit()
A.sort()
if n<=m:print(0);exit()
S = []
U = []
for i in range(1,len(A)):
    S.append(A[i]-A[i-1]-1)
    if A[i]-A[i-1]-1!=0:
        U.append(A[i]-A[i-1]-1)
T = list(set(S))
T.sort()
U.sort()
ans = 0
if len(T)==1:
    if T[0]==0:
        print(0)
    else:
        for u in U:
            ans += u//T[0]+int(u%T[0]!=0)
else:
    if T[0]==0:
        v = T[1]
    else:
        v = T[0]
    for u in U:
            ans += u//v+int(u%v!=0)
print(ans)
