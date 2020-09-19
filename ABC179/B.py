n = int(input())
D = []
for _ in range(n):
    a,b = map(int,input().split())
    D.append((a,b))
cnt = 0
for a,b in D:
    if a==b:cnt += 1
    else:
        cnt =0
    if cnt ==3:
        print('Yes');exit()
print('No')