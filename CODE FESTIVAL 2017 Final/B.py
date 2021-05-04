S = input()
a = S.count("a")
b = S.count("b")
c = S.count("c")
if abs(a-b) <=1 and abs(b-c)<=1 and abs(c-a)<=1:
    print('YES')
else:
    print('NO')