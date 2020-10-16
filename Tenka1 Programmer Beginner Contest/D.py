n = int(input())
k = int((2*n)**0.5)+1
if n!=k*(k-1)//2:
    print('No');exit()


l = [[] for _ in range(k)]
v = 1
for i in range(k):
    for j in range(k-i-1):
        l[i].append(v)
        l[i+j+1].append(v)
        v += 1
print('Yes')
print(k)
for i in range(k):
    print(k-1, *l[i])