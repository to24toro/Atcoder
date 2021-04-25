n = int(input())
s = input()
ans = float('inf')
def LCS(s1,s2):
    len1,len2 = len(s1),len(s2)
    if len1 ==0 or len2 ==0: return 0

    m = [[0 for _ in range(len2)] for _ in range(len1)]
    max_len = 0
    isSameFound = False
    for i in range(len1):
        if isSameFound or s1[i] == s2[0]:
            m[i][0] = 1
            isSameFound = True
        max_len = max(max_len,m[i][0])

    isSameFound = False
    for i in range(len2):
        if isSameFound or s2[i] == s1[0]:
            m[0][i] = 1
            isSameFound = True
        max_len = max(max_len,m[0][i])

    for i in range(0,len1-1):
        for j in range(0, len2-1):
            if s1[i+1] == s2[j+1]:
                m[i+1][j+1] = m[i][j]+1
            else:
                m[i+1][j+1] = max(m[i+1][j], m[i][j+1])
            max_len = max(max_len, m[i+1][j+1])
    return max_len
for i in range(n):
    # print(s[:i],LCS(s[:i],s[i:]))
    ans = min(ans,n-2*LCS(s[:i], s[i:]))
print(ans)
