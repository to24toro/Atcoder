S = input()
T = input()
s = len(S)
t = len(T)
f = True
ans = []
for i in range(s):
    tmp = list(S)
    if t+i>s:
        continue
    else:
        for j in range(t):
            tmp2 = list(T)
            if tmp[i+j]=='?':
                tmp[i+j] = tmp2[j]
            elif tmp[i+j]== tmp2[j]:
                continue
            else:
                f = False
        if f:
            ans.append(tmp)
    f = True
res = []
for a in ans:
    for i in range(len(a)):
        if a[i]=='?': a[i]='a'
    res.append(''.join(a))
print(min(res) if res else 'UNRESTORABLE')
        
