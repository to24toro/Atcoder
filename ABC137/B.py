k,x = map(int,input().split())
x_min = max(-1000000,x-k+1)
x_max = min(1000000,x+k-1)
a = []
for i in range(x_min,x_max+1):
    a.append(str(i))
print(' '.join(a))