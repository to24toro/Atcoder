n = int(input())
A = list(map(int,input().split()))
B = []
for a in A:
    B.append(1/a)
print(1/sum(B))