S = list(input())
N = int(input())
A = [tuple(map(int, input().split())) for i in range(N)]
 
for i in range(N):
    l = A[i][0]
    r = A[i][1]
    for j in range((r - l + 1) // 2):
        S[l - 1 + j], S[r - 1 - j] = S[r - 1 - j], S[l - 1 + j]
print("".join(S))