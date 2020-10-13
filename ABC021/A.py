n = int(input())
A = []
for i in range(4):
    if (n>>i)&1:
        A.append(2**i)
print(len(A))
for a in A:
    print(a)