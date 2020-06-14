import collections
N = int(input())
A = list(map(int,input().split()))
counter = collections.Counter(A)
B = list(set(A))
B.sort()
count = 0
for i in range(len(B)):
    if counter[B[i]]>1:
        continue
    if B[i]==1:
        count += 1
        continue
    else:
        check = 0
        for j in range(i):
            if B[j]>int(B[i]**0.5):
                break
            if (B[j] != 1 and B[i]%B[j]==0 and (B[j] in counter or B[i]//B[j] in counter)) or (B[j]==1 and B[j] in counter):
                check += 1
                break
        if check==0:
            print(B[i])
            count += 1
print(count)
    