n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = []
a = 0
b = 0
prev = 0
for i,j in zip(A,B):
    a = max(i,a)
    prev = max(prev,a*j)
    C.append(prev)
print(*C,sep = '\n')
