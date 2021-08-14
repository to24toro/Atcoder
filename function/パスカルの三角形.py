def c(n,k): 
  if(k<=0 or n<=k):
  	return 1
  else:
  	return(c(n-1, k-1) + c(n-1, k))

N=int(input())

for i in range(N):
  print([c(i,j) for j in range(i+1)])

a=[[1]]
for i in range(1,N):
    tmp=[1]
    if i >1:
        for j in range(1,i):
            tmp.append(a[i-1][j-1]+a[i-1][j])
    tmp.append(1)
    a.append(tmp)
for i in a:
    print(i)
