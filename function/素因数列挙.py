primes = [[] for _ in range(M+1)]
for p in range(2,M+1):
    if primes[p]:continue
    for i in range(p,M+1,p):
        primes[i].append(p)