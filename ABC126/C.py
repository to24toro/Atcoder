n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    s = i
    for j in range(21):
        if s>=k:
            ans += 0.5**j
            break
        s*=2
print(ans/n)