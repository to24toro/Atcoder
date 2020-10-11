D = [0]*(200001)
n = int(input())
P = list(map(int,input().split()))
s = 0
for p in P:
    D[p] += 1
    if p<=s:
        while s<200001:
            if D[s]:
                s += 1
            else:
                break
    print(s)