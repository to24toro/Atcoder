n = int(input())
def chk(s):
    for i in range(4):
        t = list(s)
        if i>=1:
            t[i],t[i-1] = t[i-1],t[i]
        if ''.join(t).count('AGC')>=1:
            return False
    return True

memo = [{} for _ in range(n+1)]
def dfs(i,l3):
    if l3 in memo[i]:
        return memo[i][l3]
    if i ==n:
        return 1
    res = 0
    for c in 'AGCT':
        if chk(l3+c):
            res += dfs(i+1,l3[1:]+c)
            res %=10**9+7
    memo[i][l3] = res
    return res

print(dfs(0,'TTT'))