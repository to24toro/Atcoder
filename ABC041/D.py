n,m = map(int,input().split())
T = [set() for _ in range(n)]
for _ in range(m):
    x,y = map(int,input().split())
    T[x-1].add(y-1)
memo = [0]*((2**n)+1)
memo[0]=1
def dp(S):
    if memo[S]>0:return memo[S]
    set_ = set()
    for i in range(n):
        if S>>i&1:
            set_.add(i)
    ans = 0
    for s in set_:#選んだbit
        flag = True
        for x in T[s]:
            if x in set_:#選んだbitから出ている点がすでに集合Sにある時はだめ
                flag = False
                break
        if flag:#上記のような点がない時sから集合Sへのパスはないのでsが一番右にきて良い
            ans += dp(S-(1<<s))
    memo[S] = ans
    return ans
print(dp(2**n-1))