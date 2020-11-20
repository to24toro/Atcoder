from itertools import permutations
A = list(map(int,input().split()))
ans = set()
for a in permutations(A):
    a = list(a)
    ans.add(sum(a[:3]))
ans = list(ans)
ans.sort(reverse =True)
print(ans[2])