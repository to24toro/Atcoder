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


#文字列S1とS2の最長共通部分を求めよ. 最長共通部分とは,
#S1とS2の要素から順番を保ったまま任意の数の文字を選択した場合に
#同一となる文字列のうち, 最長のものを指す.
#たとえば, "1224533324" と "69283746" の最長共通部分は "234"である.

def LCS(s1,s2):
    len1,len2 = len(s1),len(s2)
    if len1 ==0 or len2 ==0: return ""

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
    # return max_len
    i,j = len1-1, len2-1

    while i>=0 and j >= 0:
        if s1[i] == s2[j]:
            lcs_str += s1[i]
            i -= 1
            j -= 1
        else:
            if m[i-1][j] > m[i][j-1]:
                i -= 1
            else:
                j -= 1
    return lcs_str[::-1]