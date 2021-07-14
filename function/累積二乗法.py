def pow(x,n):
    ans = 1
    while n:
        if n&1:
            ans*=x
        x*=x
        n>>=1
    return ans

mod = 10**9+7

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



def mat_mul(a,b):
    I,J,K = len(a),len(b[0]),len(b)
    c = [[0]*J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= mod
    return c

def mat_pow(x,n):
    y = [[0]*len(x) for _ in range(len(x))]
    for i in range(len(x)):
        y[i][i] = 1
    while n:
        if n&1:
            y = mat_mul(x,y)
        x = mat_mul(x,x)
        n>>=1
    return y

