n,d,k = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(d)]
def helper(s,t):
    if s==t:return 0
    cnt = 1
    if s<t:
        for l,r in L:
            if l<=s and s<=r:
                if t<=r:
                    return cnt
                else:
                    s = r
            cnt+=1
    else:
        for l,r in L:
            if l<=s and s<=r:
                if l<=t:
                    return cnt
                else:
                    s = l
            cnt += 1
for _ in range(k):
    s,t = map(int,input().split())
    print(helper(s,t))
