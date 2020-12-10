n = int(input())
ans = 0
for i in range(1,10):
   for j in range(1,10):
      ans+=i*j
n = ans-n
A = []
for i in range(1,10):
    if n%i==0:
        if n//i<=9:
            A.append(str(i)+' x '+str(n//i))
A.sort()
for a in A:
    print(a)
