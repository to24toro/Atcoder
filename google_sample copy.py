def solve(w):
    S = sum(w)
    l,r = 0,S
    while l < r:# l = 15, r = 17
        mid = (l+r)//2
        cnt = 1
        cur = 0
        flag = True	
        for i in range(len(w)):
            if cur + w[i]<=mid:
                cur += w[i]
            else:
                cnt += 1
                cur = w[i]
            if cnt >5:
                flag = False
                break
        if flag:
            r = mid-1
        else:
            l = mid+1
    return l
w = list(map(int,input().split()))
print(solve(w))
