A = int(input())
ans = 0
for i in range(A):
    ans = max(ans,i*(A-i))
print(ans)
