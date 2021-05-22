n=int(input())
ans=[] 
for i in range(n):
    ans.append(((2*i+1)%n, (2*i+2)%n))
for a, b in ans:
    print(a+1, b+1)