A, B, C, D, E, F = map(int, input().split())

density = -1
s_water = -1
sugar = -1
for a in range(31):
    for b in range(31):
        for c in range(101):
            for d in range(101):
                w = (100*A)*a + (100*B)*b
                s = C*c + D*d
                if w == 0:
                    continue
                if w + s > F or w + s < 100*A:
                    continue
                if w/100 * E >= s:
                    tmp = 100*s / (w + s)
                    if tmp > density:
                        density = tmp
                        s_water = w + s
                        sugar = s
print(s_water, sugar)
