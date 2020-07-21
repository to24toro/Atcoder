from collections import defaultdict
dic = defaultdict(list)
for i in range(3):
    a = list(map(int,input().split()))
    for j in range(3):
        dic[a[j]].append([i,j])
n = int(input())
B = []
for _ in range(n):
    b = int(input())
    B.append(b)
h = [0]*3
w = [0]*3
d = 0
di = 0
for b in B:
    if b not in dic:
        continue
    x,y = dic[b][0]
    if x== y:
        d += 1
    if x + y ==2:
        di += 1
    h[x] += 1
    w[y] += 1
for i in range(3):
    if h[i]==3 or w[i]==3:
        print('Yes');exit()
if d ==3 or di ==3:
    print('Yes');exit()
print('No')
