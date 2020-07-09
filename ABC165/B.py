X = int(input())
a = 100
cnt = 0
while a<X:
    cnt += 1
    a *= 1.01
    a = int(a)
print(cnt)