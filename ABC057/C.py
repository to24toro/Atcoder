n = int(input())
A = []
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        if i!=n//i:
            A.append(max(i,n//i))
        else:
            A.append(i)
ans = float('inf')
for a in A:
    ans = min(ans,len(str(a)))
print(ans)


