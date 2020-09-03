s = input()
t = input()
n = len(t)
ans = float('inf')
for i in range(len(s)-n+1):
    tmp = 0
    for j in range(n):
        if t[j]!=s[i+j]:
            tmp += 1
    ans = min(ans,tmp)
print(ans if ans != float('inf') else 0)