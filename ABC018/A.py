dic = {}
A = []
B = []
for i in range(3):
    a = int(input())
    A.append(a)
    B.append(a)
A.sort(reverse = True)
for i,a in enumerate(A):
    dic[a] = i+1
for a in B:
    print(dic[a])