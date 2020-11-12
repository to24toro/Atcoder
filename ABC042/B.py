n,l = map(int,input().split())
S = []
for _ in range(n):
    S.append(input())
S.sort()
print(''.join(S))