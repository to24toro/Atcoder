n = int(input())
ans = ['']*n
for i in range(n):
    t = input()
    for j in range(n):
        ans[j]+=t[j]
for i in range(n):
    print(ans[i][::-1])