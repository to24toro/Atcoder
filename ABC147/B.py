s = input()
n = len(s)
cnt = 0
t  =s[::-1]
for i in range(n//2):
    if s[i]!=t[i]:
        cnt += 1
print(cnt)