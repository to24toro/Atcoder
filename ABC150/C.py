from itertools import permutations
N =[i+1 for i in range(int(input()))]
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
index = 0

for n in permutations(N):
    if p==n:
        x = index
    if q ==n:
        y = index

    index += 1

print(abs(x-y))