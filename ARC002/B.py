def diff(f, x, h=1e-9):
    y1 = f(x + h)
    y2 = f(x - h)
    y3 = f(x + 2 * h)
    y4 = f(x - 2 * h)
    return (y4 - 8 * y2 + 8 * y1 - y3) / (12 * h)


def fx(x): return x + P * 2 ** (-x / 1.5)


P = float(input())

l = 0
r = 200

if diff(fx, l) * diff(fx, r) > 0:
    print(P)
    exit()

for i in range(200):
    mid = (r + l) / 2
    if diff(fx, mid) * diff(fx, l) > 0:
        l = mid
    else:
        r = mid

print(fx(r))
