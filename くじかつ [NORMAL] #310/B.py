n = int(input())
S = input()
ans = 0
def helper(s,t):
    a = [0]*26
    b = [0]*26
    cnt = 0
    for i in s:
        a[ord(i)-ord('a')]+=1
    for i in t:
        b[ord(i)-ord('a')]+=1
    for i in range(26):
        if a[i]>0 and b[i]>0:
            cnt += 1
    return cnt

for i in range(1,n):
    ans = max(ans,helper(S[:i],S[i:]))
print(ans)