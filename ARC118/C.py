n = int(input())
A = [6,10,15]
if n==3:
    print(*A);exit()
# pn=[2];A=10000
# for L in range(3,A):
#     chk=True
#     for L2 in pn:
#         if L%L2 == 0:chk=False
#     if chk:pn.append(L)
set_ = set(A)
for i in range(2,10000//6):
        A.append(6*i)
        set_.add(6*i)

for i in range(1,10000//10):
    if 10*i not in set_:
        A.append(10*i)
for i in range(1,10000//15):
    if 15*i not in set_:
        A.append(15*i)

print(*A[:n])
    