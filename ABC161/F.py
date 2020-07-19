n = int(input())
if n==2:print(1);exit()
a = [n]
for i in range(2,int(n**0.5+1)):
    if n%i==0:
        a.append(i)
        if i!=n//i:
            a.append(n//i)
cnt =0
for v in a:
    s = n
    while v<=s and s%v==0:
        s = s//v
    if s%v==1: cnt += 1
b = [n-1]
m = n-1
for i in range(2,int(m**0.5+1)):
    if m%i==0:
        b.append(i)
        if i!=m//i:
            b.append(m//i)
print(cnt + len(b))