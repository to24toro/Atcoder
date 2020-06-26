a = [0]*55556
N = int(input())
for i in range(2,55556):
    for j in range(2*i,55556,i):
        a[j] += 1
A = []
for i in range(2,55556):
    if a[i]==0 and i%5==1:
        A.append(str(i))
print(' '.join(A[:N]))