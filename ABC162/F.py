n = int(input())
A = list(map(int,input().split()))
o = [0]
e = [0]
for i,a in enumerate(A):
    if i%2==1:
        e.append(e[-1]+A[i])
    else:
        o.append(o[-1]+A[i])
ans = max(o[-1],e[-1])
if n %2==0:
    for i in range(1,len(o)):
        ans = max(ans,o[i] + e[-1]-e[i])
else:
    print(o,e)
    ans = 0
    for i in range(n):
        if i%2==0:
            ans = max(ans,o[-1]-A[i])
    for i in range(1,len(o)-1):
        ans = max(ans, o[i] + e[-1]-e[i])
    for i in range(1,len(e)):
        ans = max(ans,e[i] + o[-1]-o[i+1])
    if n >5:
        new = 
        for i in range(1,len(o)-2):
            ans = max(ans,A[-1] + o[i] + e[-2]-e[i])
print(ans)
