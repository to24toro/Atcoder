a,b = map(int,input().split())
A = [a,b,a-1,b-1]
A.sort()
print(A[-1]+A[-2])