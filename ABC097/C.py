S = input()
K = int(input())
val = ''
A = set()
for i,s in enumerate(S):
    val = ''
    for j in range(i,min(i+5,len(S))):
        val += (S[j])
        A.add(val)
A_sort = sorted(list(A))
print(A_sort[K-1])