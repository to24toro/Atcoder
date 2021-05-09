k,n,m = map(int,input().split())
A = list(map(int,input().split()))
if m<=n:
    B = [(m*a)//n for a in A]
    C = []
    for i in range(k):
        C.append([A[i]/n-B[i]/m,i,B[i]])
    C.sort(reverse=True)
    diff = m-sum(B)
    # print(C)
    for i in range(diff):
        C[i][2]+=1
    C.sort(key = lambda x:x[1])
    ans = []
    for d,i,b in C:
        ans.append(b)
    print(*ans)
else:
    B = [(m*a)//n for a in A]
    C = []
    for i in range(k):
        C.append([B[i]/m-A[i]/n,i,B[i]])
    C.sort()
    diff = m-sum(B)
    for i in range(diff):
        C[i][2]+=1
    C.sort(key = lambda x:x[1])
    ans = []
    for d,i,b in C:
        ans.append(b)
    print(*ans)
