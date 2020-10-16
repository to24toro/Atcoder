N = int(input())
A = list(map(int, input().split()))
flag = True
s = 0
cnt1 = 0
cnt2 = 0
for a in A:
    s += a
    if flag:
        x = max(0, 1 - s)
        cnt1 += x
        s += x
        flag = False
    else:
        x = max(0, s + 1)
        cnt1 += x
        s -= x
        flag = True
flag = False
s = 0
for a in A:
    s += a
    if flag:
        x = max(0, 1 - s)
        cnt2 += x
        s += x
        flag = False
    else:
        x = max(0, s + 1)
        cnt2 += x
        s -= x
        flag = True

print(min(cnt1, cnt2))