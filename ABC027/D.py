S = input()
p = 0
for s in S:
    if s=='+':
        p += 1
    elif s=='-':
        p-=1
l = []
for s in S:
    if s=='M':
        l.append(p)
    elif s=='+':
        p-=1
    else:
        p+=1
l.sort()
n = len(l)//2
print(sum(l[n:])-sum(l[:n]))
