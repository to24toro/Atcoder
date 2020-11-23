a,b,c = map(int,input().split())
n = 300
frac = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]//(frac[n-r]*frac[r])
ans = 0
for i in range(a,101):
    for j in range(b,101):
        for k in range(c,101):
            if (i==100 and i==j) or (j==100 and k==j) or (k==100 and i==k):
                continue
            if i!=100 and j!=100 and k!=100:
                continue
            A = i-a
            B = j-b
            C = k-c
            m = A+B+C
            tmp = (frac[a+A-1]*frac[b+B-1]*frac[c+C-1]*frac[a+b+c-1])/(frac[a-1]*frac[b-1]*frac[c-1]*frac[m+a+b+c-1])
            if i==100:
                A-=1
            elif j==100:
                B-=1
            else:
                C-=1
            ans +=m*nCr(A+B+C,A)*nCr(B+C,B)*tmp
print(ans)


