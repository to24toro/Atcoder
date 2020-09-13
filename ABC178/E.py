n = int(input())
x = []
y = []
for _ in range(n):
    X,Y = map(int,input().split())
    x.append(X)
    y.append(Y)

res = 0
for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
    smallest = p * x[0] + q * y[0] + 0
    for i in range(n):
        cur = p * x[i] + q * y[i]
        res = max(res, cur - smallest)
        smallest = min(smallest, cur)
print(res)

