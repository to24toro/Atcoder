M=10**9+7
n,k=map(int,input().split())
l=[0]*(k+1)
a=0
for i in range(k,0,-1):
  l[i]=pow(k//i,n,M)
  for j in range(i*2,k+1,i):
    l[i]-=l[j]
  a+=i*l[i]
print(a%M)
