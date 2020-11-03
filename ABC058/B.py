a = input()
b = input()
ans =''
for i in range(len(b)):
    ans += a[i]+b[i]
if len(a)>len(b):
    ans += a[-1]
print(ans)