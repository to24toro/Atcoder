N = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
A = [a[0]]
for i in range(1,N):
    A.append(a[i])
    A.append(a[i])
print(sum(A[:N-1]))