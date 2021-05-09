n,k = map(int,input().split())
for _ in range(k):
    if n%200:
        n = int(str(n)+'200')
    else:
        n//=200
print(n)