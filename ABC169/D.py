def factorization(n):
    res = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            res.append([i, cnt])
 
    if tmp!=1:
        res.append([tmp, 1])
 
    return res

N = int(input())
ans = 0
for tmp,cnt in factorization(N):
    i = 1
    while i<=cnt:
        ans += 1
        cnt-=i
        i += 1
print(ans)