n = int(input())
A = []
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        A.append(i)
        if n//i !=i:
            A.append(n//i)
A.sort()
for a in A:
    print(a)