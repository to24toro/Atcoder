D = [0]*26
n = int(input())
S  = []
for _ in range(n):
    S.append(input())
for s in S:
    d = [0]*26
    for i in s:
        d[ord(i)-ord('a')] += 1
    f = True
    for i in range(26):
        if f and D[i]>d[i]:
            D[i] = d[i]
        if not f:
            D[i] = d[i]

ans = 0
for i in range(26):
    ans += D[i]
print(ans)