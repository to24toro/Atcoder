n = int(input())
S = input()
r = S.count('R')
g = S.count('G')
b = S.count('B')
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if S[i]!=S[j]:
            k = 2*j-i
            if k<n and S[k]!=S[i] and S[k]!=S[j]:
                cnt += 1
print(r*g*b-cnt)