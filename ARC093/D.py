a,b = map(int,input().split())
S = [["."]*100 for _ in range(50)]+[["#"]*100 for _ in range(50)]
# print(S)
a-=1
b-=1
for i in range(0,50,2):
    for j in range(0,100,2):
        if b>0:
            S[i][j]="#"
            b-=1
# print(a)
for i in range(99,49,-2):
    for j in range(0,100,2):
        # print(a)
        if a>0:
            # print(i,j)
            S[i][j]="."
            a-=1
print(100,100)
for s in S:
    print(''.join(s))


