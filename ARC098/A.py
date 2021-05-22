ans = float('inf')
n = int(input())
for b in range(100):
    B = pow(2,b)
    tmp = n//B
    c = n-tmp*B
    if tmp>=0 and b>=0 and c>=0:
        ans = min(ans,b+c+tmp)
print(ans)