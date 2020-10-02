n = int(input())
A = list(map(int,input().split()))
even = []
odd = []
four = []
for a in A:
    if a%4==0:
        four.append(a)
    elif a%2==0:
        even.append(a)
    else:
        odd.append(a)
if len(four)>=len(odd):
    print('Yes');exit()
elif len(four)+1==len(odd):
    if len(even):
        print('No')
    else:
        print('Yes')
else:
    print('No')