h,w,k = map(int,input().split())
S = [input() for _ in range(h)]
ans = float('inf')
for bit in range(1<<(h-1)):
    segment = [0]*h
    seg = 0
    for i in range(h-1):
        if bit & (1<<i):
            seg += 1
        segment[i+1] = seg
    n = max(segment) + 1

    count = n-1
    k_cnt = [0]*n
    for j in range(w):
        tmp = [0]*n
        for i in range(h):
            k_cnt[segment[i]] += int(S[i][j])
            tmp[segment[i]] += int(S[i][j])
            if k_cnt[segment[i]] > k:
                count += 1
                for i in range(n):
                    k_cnt[i] = tmp[i]
    ans = min(ans,count)
print(ans)