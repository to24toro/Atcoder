n = int(input())
o = 0
e = 0
R = [int(input()) for _ in range(n)]
R.sort(reverse = True)
ans = 0
for i in range(n):
    if i%2==0:
        ans += 3.14159265*R[i]**2
    else:
        ans-=3.14159265*R[i]**2
print(ans)