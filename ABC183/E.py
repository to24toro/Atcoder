h, w = map(int, input().split()); s = []
for _ in range(h): s.append(input())
a = [0]*h
b = [0]*w
c = [0]*(h+w-1)
mod = 10**9+7
a[0] = b[0] = c[h-1] = 1

for i in range(h):
    for j in range(w):
        if i==0 and j==0:continue
        if s[i][j] =='#':
            a[i] = b[j] = c[h-1-i+j] = 0
        else:
            x = a[i] + b[j] + c[h-1-i+j]
            a[i] = (a[i] +x)%mod
            b[j] = (b[j]+x)%mod
            c[h-1-i+j] =(c[h-1-i+j]+x)%mod
print(x%mod)