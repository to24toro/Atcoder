s = input()
n =int(input())
A = []
for i in range(len(s)):
    for j in range(len(s)):
        A.append(s[i]+s[j])
A.sort()
print(A[n-1])