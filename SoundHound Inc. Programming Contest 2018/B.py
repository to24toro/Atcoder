s = input()
w = int(input())
ans = ''
for i in range(len(s)):
    if i%w==0:
        ans += s[i]
print(ans)