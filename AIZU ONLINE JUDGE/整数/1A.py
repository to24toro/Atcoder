n = int(input())

def prime_factorization(n):#素数を返答
    ans = []
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            while n%i==0:
                n//=i
                ans.append(i)
        if n==1:
            return ans
    ans.append(n)
    return ans
ans = prime_factorization(n)

print(str(n)+': '+' '.join(map(str,ans)))
