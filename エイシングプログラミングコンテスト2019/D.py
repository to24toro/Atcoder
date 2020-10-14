n,m = map(int,input().split())
A = list(map(int,input().split()))
if n%2:A+=[0];n+=1
A.sort()
S = [0]*(n+1)
S2 = [0]*(n+1)
for i in range(n):S[i+1]=S[i]+A[i]
for i in range(0,n-1):S2[i+2]=S2[i]+A[i]
def calc(p):
    f = S[-1]-S[-p-1]
    f+=S2[-2*p]
    return f
def ch(x,p):
    maxa=A[-p-1]
    mina=A[-2*p+1]
    diff=A[-p]-x
    if diff<0:
        return False
    if x-diff<=mina and maxa<=x+diff:
        return True
    return False
for _ in range(m):
    x = int(input())
    ng,ok = n//2+1,1
    while ng-ok>1:
        mid = (ng+ok)//2
        if ch(x,mid):ok = mid
        else:ng = mid
    print(calc(ok))