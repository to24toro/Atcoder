N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

INF = 10 ** 18 + 1
l, r = -INF, INF
while l + 1 < r:
    x = (l + r) // 2

    cnt = 0
    for a in A:
        if a < 0:
            l2, r2 = -1, N
            while l2 + 1 < r2:
                c2 = (l2 + r2) // 2
                if A[c2] * a < x:
                    r2 = c2
                else:
                    l2 = c2
            cnt += N - r2
        else:
            l2, r2 = -1, N
            while l2 + 1 < r2:
                c2 = (l2 + r2) // 2
                if A[c2] * a < x:
                    l2 = c2
                else:
                    r2 = c2
            cnt += r2
        if a * a < x:
            cnt -= 1
    cnt //= 2
    ok = cnt < K

    if ok:
        l = x
    else:
        r = x
print(l)
