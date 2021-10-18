# n = int(input())
# A = list(map(int,input().split()))
# p = A[0]
# ans = 0
# cnt = 1
# for i in range(1,n):
#     if p==A[i]:
#         cnt += 1
#     else:
#         if cnt%2==0:
#             ans += (cnt//2)**2
#             cnt = 1
#         else:
#             cnt-=1
#             ans += cnt*(cnt+1)
#             cnt = 1
#         p = A[i]
#         print(p,ans,i)
# B = [(A[0],1)]
# p = A[0]
# cnt = 1
# for i in range(1,n):
#     if p!=A[i]:
#         B.append((A[i],cnt))
#         p = A[i]
#         cnt = 1
#     else:
#         cnt += 1
# for i in range(1,len(B)-1):
#     if B[i][0]==B[i-1][0]+B[i+1][0]:
#         ans += (B[i-1][1]//2)*(B[i+1]//2)

# C = []
# cnt = 0
# p = A[0]
# for i in range(1,n):
#     if p!=A[i]:
#         if cnt!=0:
#             cnt = 0
#             p = A[i]
#         else:
#             C.append(p)
#             p = A[i]
#             cnt = 0
#     else:
#         cnt += 1
# if p!=C[-1]:
#     C.append(p)
# p = -float('inf')
# cnt = 1
# for i in range(1,len(C)-1):
#     tmp = C[i]-C[i-1]-C[i+1]
#     if tmp>0:
#         if tmp==p:
#             cnt += 1
#         else:
#             if cnt%2==0:
#                 ans += (cnt//2)**2
#                 cnt = 0
#             else:
#                 cnt-=1
#                 ans += cnt*(cnt+1)
#             p = tmp
#             cnt = 1
# if cnt>1:
#     if cnt%2==0:
#         ans += (cnt//2)**2
#         cnt = 0
#     else:
#         cnt-=1
#         ans += cnt*(cnt+1)
# print(ans)

from collections import defaultdict


n,m = map(int,input().split())
class  MultipleFactorization:
    def __init__(self,n):
        self.data = [i for i in range(n+1)]
        self.n = n
        self._get_sieve()
    def _get_sieve(self):
        import math
        for i in range(2,int(math.sqrt(self.n))+1):
            if self.data[i]!=i:
                continue
            j = i
            while j <=self.n:
                if self.data[j]==j:
                    self.data[j] = i
                j +=i
    def prime(self):
        res = []
        for i in range(2,self.n+1):
            if self.data[i]==i:
                res.append(i)
        return res
    def factorization(self,x):
        factors = []
        while x > 1:
            k = self.data[x]
            factors.append(k)
            x //= k
        return factors
    def count_prime(self,x):
        cnt = 0
        s = set()
        while x>1:
            k = self.data[x]
            if k not in s:
                cnt += 1
                s.add(k)
            x//=k
        return cnt
multi = MultipleFactorization(m)
L = multi.prime()
M = m

dic = defaultdict(int)
ans = 0
mod = 998244353
n+=m
frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+1):
    finv[n-i] = finv[n-i+1]*(n-i+1)%mod
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]*finv[n-r]*finv[r]%mod
n-=m
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
for i in range(1,m+1):
    M = i
    dic = defaultdict(int)
    L = make_divisors(M)
    for l in L[1:]:
        while M%l==0 and M!=1:
            dic[l]+=1
            M//=l
        if M==1:
            break
    res =1
    for k,v in dic.items():
        res *= nCr(n+v-1,v)
        res%=mod
    ans += res
    ans%=mod
print(ans)
