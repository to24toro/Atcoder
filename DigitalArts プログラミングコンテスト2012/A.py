S = input().split()
N = int(input())
t = [str(input()) for _ in range(N)]
ans = []
for i in S:
  for j in t:
    if len(i) == len(j) and all([a == b for a, b in zip(i, j) if b != "*"]):
      ans.append("*" * len(i))
      break
  else:
    ans.append(i)
print(*ans)