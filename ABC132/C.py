n = int(input())
D = list(map(int,input().split()))
D.sort()
a = D[n//2]
b = D[n//2-1]
print(a-b)