n = int(input())
A = list(map(int,input().split()))
val1 = sum(A)//n
val2 = val1+1
ans1 = 0
ans2 = 0
for a in A:
    ans1 += (a-val1)**2
    ans2 += (a-val2)**2
print(min(ans1,ans2))
