n = int(input())
A = list(map(int,input().split()))
A.sort()
X = A[-1]
x = A[0]
while A:
    i = 0
    tmp = []
    while i<len(A):
        if A[i]==x:
            tmp.append(A[i])
        elif A[i]%x!=0:
            tmp.append(A[i]%x)
        i += 1

    A = tmp
    if x==min(A): break
    x = min(A)
print(min(A))