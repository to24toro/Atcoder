#与えられた２つの文字列に対し, 共通で持つ部分文字列の最大長を求めよ.
#例) "abcdefg" と "cdeg" が与えられたとして, 最大の部分文字列は "cde" なので答えは３.

def LCS(s1,s2):
    if not s1 or not s2:
        return 0
    len1, len2 = len(s1), len(s2)

    m = [[0 for _ in range(len2)] for _ in range(len1)]

    lcs = 0

    for i,x in enumerate(s1):
        if x == s2[0]:
            m[i][0] = 1
            lcs = 1
    for i,x in enumerate(s2):
        if x == s1[0]:
            m[0][i] = 1
            lcs = 1
    
    for i in range(1,len1):
        for j in range(1,len2):
            if s1[i] == s2[j]:
                m[i][j] = m[i-1][j-1] + 1
                lcs = max(m[i][j],lcs)
            else:
                m[i][j] = 0
    return lcs