s = input()
h = s.count('?')
m = s.count('o')
b = s.count('x')
if m>4:
    print(0)
elif m ==4:
    print(24)
elif m==3:
    ans = 24*h+12*3
    print(ans)
elif m==2:
    ans = 2*4+6+12*h*2+6*h*h*2
    print(ans)
elif m==1:
    ans = 1+6*h*h+4*h+4*h*h*h
    print(ans)
else:
    ans = h**4
    print(ans)