n,m,k = map(int,input().split())
A = list(map(int,input().split()))
M = [[0]*n for _ in range(n)]
g = [[] for _ in range(n)]
mod = 10**9+7
invM=pow(m,mod-2,mod)
inv2=pow(2,mod-2,mod)

for _ in range(m):
    x,y = map(lambda x:int(x)-1 ,input().split())
    g[x].append(y)
    g[y].append(x)


for i in range(n):
    M[i][i] = ((m-len(g[i]))*invM+len(g[i])*inv2*invM)%mod
    for j in g[i]:
        M[j][i] = invM*inv2%mod
def m(a,b):
    r=[[0]*len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            for j in range(len(b[0])):
                r[i][j]=(r[i][j]+a[i][k]*b[k][j])%mod
    return r
 
def p(a,n):
  r=[[0]*len(a) for i in range(len(a))]
  b=[]
  for i in range(len(a)):
    r[i][i]=1
    b.append(a[i][:])
  l=n
  while l>0:
    if l&1:
      r=m(b,r)
    b=m(b,b)
    l>>=1
  return r

Y=[[0]*n for i in range(n)]
for i in range(n):
  Y[i][-1]=A[i]
Z=m(p(M,k),Y)
for i in range(n):
  print(Z[i][-1])
