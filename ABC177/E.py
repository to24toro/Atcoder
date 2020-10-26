import math

n = int(input())
A = list(map(int,input().split()))
maxa = max(A)
d = [0]*(maxa+1)

#素数列挙関数###################################
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
 
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
 
    divisors.sort()
    return divisors
 
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
 
    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table
##############################################
gcd = A[0]
is_prime,table = sieve(10**6)
f = True
for a in A:
    d[a]+=1
for i in range(2,maxa+1):
    idx = i
    cnt=0
    while idx<=maxa:
        cnt+=d[idx]
        idx+=i
    if cnt>=2:
        f = False
        break
if f:
    print("pairwise coprime");exit()
for a in A:
    gcd = math.gcd(gcd,a)
if gcd==1:
    print("setwise coprime");exit()
print("not coprime")

