n,m = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
x = 0
y = 0
for i in range(n):
    x += (i)*X[i] -(n-i-1)*X[i]
for i in range(m):
    y += (i)*Y[i] -(m-i-1)*Y[i]
mod = 10**9+7
print(x*y%mod)