a,b,c,d,e = map(int,input().split())
A = [a,b,c,d,e]
for i in range(len(A)):
    if A[i]==0:
        print(i+1)
        break