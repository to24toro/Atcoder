n = int(input())
A = []
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        if n//i!=i:
            A.append((i,n//i))
        else:
            A.append((i,i))
ans = float('inf')
for a,b in A:
    a-=1
    b-=1
    ans = min(ans, a+b)
# print(A)
print(ans)