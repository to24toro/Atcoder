n = int(input())
s = input()
a ='11'
b = '10'
c = '01'
d = '00'
A,B,C,D = False,False,False,False
for i in range(1,n):
    if s[i]=='o':
        if a[i]=='1':
            a += a[i-1]
        else:
            a += str(1-int(a[i-1]))
    else:
        if a[i]=='1':
            a += str(1-int(a[i-1]))
        else:
            a += a[i-1]
if a[0] != a[-1]:A = True
else:
    a = a[:-1]
    if s[0]=='o' and a[1] ==a[-1]:
        print(a.replace('1','S').replace('0','W'));exit()
    elif s[0] =='x' and a[1] !=a[-1]:
        print(a.replace('1','S').replace('0','W'));exit()

for i in range(1,n):
    if s[i]=='o':
        if b[i]=='1':
            b += b[i-1]
        else:
            b += str(1-int(b[i-1]))
    else:
        if b[i]=='1':
            b += str(1-int(b[i-1]))
        else:
            b += b[i-1]
if b[0] != b[-1]:B = True
else:
    b = b[:-1]
    if s[0]=='o' and b[1] ==b[-1]:
        print(b.replace('1','S').replace('0','W'));exit()
    elif s[0] =='x' and b[1] !=b[-1]:
        print(b.replace('1','S').replace('0','W'));exit()
for i in range(1,n):
    if s[i]=='o':
        if c[i]=='1':
            c += c[i-1]
        else:
            c += str(1-int(c[i-1]))
    else:
        if c[i]=='1':
            c += str(1-int(c[i-1]))
        else:
            c += c[i-1]
if c[0] != c[-1]:C = True
else:
    c = c[:-1]
    if s[0]=='o' and c[1] !=c[-1]:
        print(c.replace('1','S').replace('0','W'));exit()
    elif s[0] =='x' and c[1] ==c[-1]:
        print(c.replace('1','S').replace('0','W'));exit()
for i in range(1,n):
    if s[i]=='o':
        if d[i]=='1':
            d += d[i-1]
        else:
            d += str(1-int(d[i-1]))
    else:
        if d[i]=='1':
            d += str(1-int(d[i-1]))
        else:
            d += d[i-1]
if d[0] != d[-1]:D = True
else:
    d = d[:-1]
    if s[0]=='o' and d[1] !=d[-1]:
        print(d.replace('1','S').replace('0','W'));exit()
    elif s[0] =='x' and d[1] ==d[-1]:
        print(d.replace('1','S').replace('0','W'));exit()

if A or B or C or D:
    print(-1)