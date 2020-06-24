N = int(input())
A = list(map(int,input().split()))
ans = 0
total = A[0]
l=r=0
xor = A[0]

while True:
    if xor==total:
        ans += r-l+1
        r += 1
        if r==N:
            break
        total += A[r]
        xor ^= A[r]
    else:
        total -= A[l]
        xor ^= A[l]
        l += 1
    
print(ans)