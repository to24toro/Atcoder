n = int(input())
A = list(map(int,input().split()))
ans = 0
for a in A:
    if a % 2 == 0:
        if (a - 1) % 3 == 2:
            ans += 3
        else:
            ans += 1
    else:
        if a % 3 == 2:
            ans += 2
        else:
            continue
print(ans)