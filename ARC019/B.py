S = input()
n = len(S)
a = S[:n//2]
if n%2:
    b = S[n//2+1:]
else:
    b = S[n//2:]
ans = 1
b = S[::-1]
cnt = 0
if n==1:
    print(0);exit()
for i,j in zip(a,b):
    if i!=j:
        cnt += 1
if cnt==0:
    print(n//2*2*25)
elif cnt==1:
    print((n//2*2-2)*25+24*2+25*(n%2))
else:
    print(25*n)