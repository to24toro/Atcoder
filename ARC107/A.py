a,b,c = map(int,input().split())
A = a*(a+1)//2
B = b*(b+1)//2
C = c*(c+1)//2
print(A*B*C%998244353)