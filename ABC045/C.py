S = input()
n = len(S)
ans = 0
if n==1:print(S);exit()
for bit in range(1<<(n-1)):
    s,t = 0,0
    f = False
    for j in range(n-1):
        if (bit>>j)&1:
            f = True
            t = j+1
            ans += int(S[s:t])
            s = t
    if f:ans += int(S[s:])
print(ans+int(S))
