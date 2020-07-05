s = input()
x, y = map(int, input().split())
y = abs(y)

f = s.find('T')
if f >= 0:
    x = abs(x - f)
    s = s[f:]
else:
    if x == len(s) and y == 0:
        print('Yes')
    else:
        print('No')
    exit()

lx, ly = [], []
flag = True
n = 0
s += 'T'
for i in s:
    if i == 'F':
        n += 1
    else:
        if n > 0:
            if flag:
                lx.append(n)
            else:
                ly.append(n)
            n = 0
        flag = not flag

lx.sort()
ly.sort()
sx = sum(lx)
sy = sum(ly)

if sx < x or (sx - x) % 2 == 1 or sy < y or (sy - y) % 2 == 1:
    print('No')
    exit()


def main(x, sx, lx):
    if x == sx:
        return True

    goal = (sx - x) // 2
    # return (sum of some lx == goal)
    dp = [False] * (goal + 1)
    dp[0] = True
    for i in lx:
        if i > goal:
            return False
        for j in range(goal - i, -1, -1):
            if dp[j]:
                dp[j+i] = True
        if dp[goal]:
            return True
    return False


if main(x, sx, lx) and main(y, sy, ly):
    print('Yes')
else:
    print('No')
