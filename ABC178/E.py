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

#There are two ways to make the walk. 
# Either we have four corners, as @carl5 pointed out,
#  and have all individual points go to all the corners. 
# Or, we have one endpoint (0, 0), as the solution suggested, and have all individual points go to (0, 0) in four directions: