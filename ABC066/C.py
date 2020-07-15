n = int(input())
a = list(map(int,input().split()))
x = []
y = []
for i in range(len(a)):
    if i%2==0:
        x.append(str(a[i]))
    else:
        y.append(str(a[i]))
if n%2==1:
    x = x[::-1]
    print(' '.join(x+y));exit()
else:
    y = y[::-1]
    print(' '.join(y+x));exit()