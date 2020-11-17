MOD = 10007
A = [0]*(1000001)
n = int(input())
A[3] = 1
for i in range(4,len(A)):
    A[i] = A[i-1]+A[i-2]+A[i-3]
    A[i]%=MOD
print(A[n]%MOD)