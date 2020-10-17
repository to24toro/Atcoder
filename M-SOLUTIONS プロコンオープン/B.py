s = input()
k = len(s)
if k<8:
    print('YES');exit()
batu = s.count('x')
if batu>7:
    print('NO')
else:
    print('YES')