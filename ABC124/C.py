s = input()
n = len(s)
cnt1 = 0
cnt2 = 0
for i in range(n):
    if i%2:
        if s[i]=='0':
            cnt1 += 1
    else:
        if s[i]=='1':
            cnt1 += 1
for i in range(n):
    if i%2:
        if s[i]=='1':
            cnt2 += 1
    else:
        if s[i]=='0':
            cnt2 += 1
print(min(cnt1,cnt2))