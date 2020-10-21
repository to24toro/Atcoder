N,A,B,C = map(int,input().split())
S = []
d = {'A':A,'B':B,'C':C}
for _ in range(N):
    S.append(input())

ans = []

for i,s in enumerate(S):
    if d[s[0]]==0 and d[s[1]] ==0:
        print('No');exit()
    else:
        if d[s[0]]>d[s[1]] or (d[s[0]]==d[s[1]] and i<N-1 and s[1] in S[i+1]):
            d[s[1]] += 1
            d[s[0]] -= 1
            ans.append(s[1])
        else:
            d[s[0]] += 1
            d[s[1]] -= 1
            ans.append(s[0])
print('Yes')
for a in ans:
    print(a)