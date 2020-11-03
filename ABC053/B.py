S = input()
a = -1
for i,s in enumerate(S):
    if s=='A' and a==-1:
        a = i
    elif s =='Z':
        b =i
print(b-a+1)
