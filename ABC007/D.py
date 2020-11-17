a,b = map(int,input().split())
def f(S):
    dp = [[[0]*2 for _ in range(2)] for _ in range(20)]
    dp[0][0][0] = 1
    L = len(S)
    for i in range(L):
        D = int(S[i])
        for j in range(2):
            for k in range(2):
                if j:
                    num = 9
                else:
                    num = D
                for d in range(num+1):
                    dp[i+1][j or(d<D)][k or d==4 or d==9]+=dp[i][j][k]
    return dp[L][0][1]+dp[L][1][1]
print(f(str(b))-f(str(a-1)))