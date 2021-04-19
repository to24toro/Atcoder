def Z_algorithm(s):
    N = len(s)
    Z_alg = [0]*N

    Z_alg[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_alg[k]<j:
            Z_alg[i+k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return Z_alg
n = int(input())
S = input()
ans = 0
for i in range(n):
    s = S[i:]
    Z = Z_algorithm(s)
    for j in range(len(Z)):
        if Z[j]<j+1:
            ans = max(ans,Z[j])
# S = S[::-1]
# for i in range(n):
#     s = S[:i+1]
#     Z = Z_algorithm(s)
#     for j in range(len(Z)):
#         if Z[j]<j+1:
#             ans = max(ans,Z[j])
print(ans)
