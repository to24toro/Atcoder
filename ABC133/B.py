n,D = map(int,input().split())
X  =[]
for _ in range(n):
    x = list(map(int,input().split()))
    X.append(x)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        val = 0
        for d in range(D):
            val += (X[i][d]-X[j][d])**2
        val = val**0.5
        if val.is_integer():
            ans += 1
print(ans)
        
