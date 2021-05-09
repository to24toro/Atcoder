n,k = map(int,input().split())
a = 1
cnt = 3
K = k
while k-a>0:
    k-=a
    a*=3
    cnt +=1
b = pow(2,cnt-3)
i = 1
print(k,cnt)
while k-b>=0 and i<=n:
    k-=b
    b//=2
    i += 1
print(i)
ans1 = i
j = cnt-i-1

if j<=n:
    print(ans1,1,j)
else:
    ans2 = cnt-i-n
    print(ans1,ans2,n) 


