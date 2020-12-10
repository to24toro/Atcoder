s = input()
i = 1
n = len(s)
cnt = 1
x = s[0]
ans=''
if n==1:print(s+'1');exit()
while i<n:
    a = s[i]
    if x==a:
        cnt += 1
        i+=1
    else:
        ans += x+str(cnt)
        x = s[i]
        cnt = 1
        i+=1
    if i==n:
        ans+=x+str(cnt)
print(ans)
