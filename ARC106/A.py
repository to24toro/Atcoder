n = int(input())
a = []
b = []
s = 1
for i in range(40):
    s *= 3
    a.append(s)
s = 1
for i in range(26):
    s*=5
    b.append(s)
for i in range(40):
    for j in range(26):
        if a[i]+b[j] ==n:
            print(i+1,j+1);exit()
print(-1)
