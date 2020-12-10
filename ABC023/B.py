n = int(input())
S = input()
s = S[n//2]
if n%2==0:print(-1);exit()
if s!='b':print(-1);exit()
for i in range(n-1):
    if S[i]=='a':
        if S[i+1]!='b':
            print(-1);exit()
    elif S[i]=='b':
        if S[i+1]!='c':
            print(-1);exit()
    else:
        if S[i+1]!='a':
            print(-1);exit()
print((n-1)//2)